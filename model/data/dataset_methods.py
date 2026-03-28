import torch
def build_vocab(data: list[str]) -> tuple[dict,dict,int]:
    """
    Builds a vocabulary using the data, taking into account unknown words and padding.

    param data: Content, particularly multiple strings put together to form a paragraphs.
    return data_idx: The vocabulary with the data mapped to the indices.
    return idx_data: The vocabulary with the indices mapped to the data.
    """
    seen = set()
    data_idx = {}
    idx_data = {}
    count = 2
    data_idx['<PAD>'], data_idx['<UNK>'], idx_data[0],idx_data[1] = 0, 1, '<PAD>', '<UNK>'
    
    for i in data:
        for y in i.split():
            y = y.strip(',."\'()')
            if y in seen:
                continue
            else:
                seen.add(y)
                data_idx[y] = count
                idx_data[count] = y
                count += 1
    return data_idx, idx_data, count

def tokens_vocab(tokens, data_idx):
    """
    Converts a list of tokens into the indices.

    param tokens: A string.
    return indices: A list of the tokens converted to indices
    """
    indices = []
    for i in tokens.split():
        if i in data_idx:
            indices.append(data_idx[i])
        else:
            indices.append(1)
    return indices

def collate_fn(batch):
    """
    Combines a list of samples into a batch.
    param batch: The list of samples to combine
    return padded_tokens: The original tokens with padding
    return padded_labels: The original labels with padding
    """

    tokens, labels = zip(*batch)
    
    max_len = len(max(tokens, key=len))
    
    padded_tokens = [t + [0] * (max_len - len(t)) for t in tokens]
    padded_labels = [l + [0] * (max_len - len(l)) for l in labels]
    
    return torch.tensor(padded_tokens), torch.tensor(padded_labels)



