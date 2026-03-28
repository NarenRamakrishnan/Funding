import torch
import torch.nn as nn

class FundingNER(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers, dropout, num_classes=6):
        super().__init__() #required when inheriting from nn
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0) #Creates vectors for each token
        self.bilstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=num_layers, 
                              batch_first=True, bidirectional=True) #batch_first tells python to expect batchsize,seqlen,features, matches dataloader
        self.dropout = nn.Dropout(dropout) #reduces overfitting
        self.fc = nn.Linear(hidden_dim * 2, num_classes) #Final layer

    def forward(self, x):
        embedded = self.embedding(x)
        out, _ = self.bilstm(embedded)
        out = self.dropout(out)
        out = self.fc(out)
        return out