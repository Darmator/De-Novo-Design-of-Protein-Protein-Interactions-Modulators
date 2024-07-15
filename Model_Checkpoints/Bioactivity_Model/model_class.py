class DualMultiPPIMI(nn.Module):
    def __init__(self, modulator_model, modulator_emb_dim, ppi_emb_dim, 
                 h_dim, n_heads, 
                 output_dim=1, dropout=0.2, device=None, attention=False):
        super(DualMultiPPIMI, self).__init__()
        self.attention = attention
        self.modulator_emb_dim = modulator_emb_dim
        self.ppi_emb_dim = ppi_emb_dim
        self.modulator_model = modulator_model

        ##### bilinear attention #####
        self.bcn = weight_norm(
            BANLayer(v_dim=modulator_emb_dim, q_dim=ppi_emb_dim, h_dim=h_dim, h_out=n_heads, k=3),
            name='h_mat', dim=None)

        self.fc1 = nn.Linear(h_dim, 1024)
        self.fc2 = nn.Linear(1024, 256)
        self.out_reg = nn.Linear(256+1, output_dim)
        self.out_class = nn.Linear(256, output_dim)
        self.pool = global_mean_pool
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)
        self.bn_1 = nn.BatchNorm1d(1024)
        self.bn_2 = nn.BatchNorm1d(256)

    def forward(self, modulator, rdkit_descriptors, ppi_feats, regression = True, classification = True):
        modulator_node_repr = self.modulator_model(modulator)
        modulator_repr = self.pool(modulator_node_repr, modulator.batch)
        modulator_repr = torch.cat((modulator_repr, rdkit_descriptors), 1)

        

        x, att = self.bcn(modulator_repr, ppi_feats)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.bn_1(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.bn_2(x)
        x_2 = self.out_class(x)
        if(regression):
            x = torch.cat((x, x_2), 1)
            x_1 = self.out_reg(x)
            if(classification):
                return x_1, x_2
            else:
                return x_1
        else:
            return x_2