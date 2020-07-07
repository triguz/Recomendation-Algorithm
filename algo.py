import numpy as numpi
import surprise

class RecAlgo(surprise.AlgoBase):
    '''Un banale algoritmo per sistemi di raccomandazione.'''
    
    def __init__(self, learning_rate, n_epochs, n_factors):
        
        self.lr = learning_rate  # tasso di apprendimento per SGD
        self.n_epochs = n_epochs  # numero di iterazioni per SGD
        self.n_factors = n_factors  # numero di fattori 
        
    def fit(self, trainset):
        '''Popola i vettori p_u e q_i tramite SGD'''
        
        print('Popolazione dei dati tramite SGD...')
        
        # Inizializzazione randomica dei fattori per utenti e item.
        p = numpi.random.normal(0, .1, (trainset.n_users, self.n_factors))
        q = numpi.random.normal(0, .1, (trainset.n_items, self.n_factors))
        
        # Procedura SGD
        for _ in range(self.n_epochs):
            for u, i, r_ui in trainset.all_ratings():
                err = r_ui - numpi.dot(p[u], q[i])
                # Aggiorno i vettori p_u e q_i
                p[u] += self.lr * err * q[i]
                q[i] += self.lr * err * p[u]
        
        self.p, self.q = p, q
        self.trainset = trainset

    def estimate(self, u, i):
        '''Rende la valutazione/rating stimato dell'utente u per l'item i.'''
        
        # Rende un prodotto scalare tra p_u e q_i se l'utente e l'item sono conosciuti, altrimenti rende una media di tutti i ratings
        if self.trainset.knows_user(u) and self.trainset.knows_item(i):
            return numpi.dot(self.p[u], self.q[i])
        else:
            return self.trainset.global_mean



# Caricamento del db, utilizziamo il Movielens DataSet (https://grouplens.org/datasets/movielens/100k/)
# Grazie alla libreria Surprise possiamo scaricarlo automaticamente.
data = surprise.Dataset.load_builtin('ml-100k')
data.split(2)  # Divide i dati per 2-folds cross validation


algo = RecAlgo(learning_rate=.01, n_epochs=10, n_factors=10)
surprise.evaluate(algo, data, measures=['RMSE'])
surprise.evaluate(algo, data, measures=['mae'])


# Utilizziamo un algoritmo di neighborhood sugli stessi dati come confronto
algo = surprise.KNNBasic()
surprise.evaluate(algo, data, measures=['RMSE'])
surprise.evaluate(algo, data, measures=['mae'])


# Utilizziamo un metodo di fattorizzazione piu sofisticato sugli stessi dati
algo = surprise.SVD()
surprise.evaluate(algo, data, measures=['RMSE'])
surprise.evaluate(algo, data, measures=['mae'])
