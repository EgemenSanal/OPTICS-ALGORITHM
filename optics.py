import pandas as pd #excel dosyasından veriyi okumak için gereken kütüphane
from sklearn.cluster import OPTICS #scikit-learn kütüphanesi ile OPTICS sınıfını kullanarak OPTICS algoritmsaını uyguluyoruz.

# Excel dosyasından veri okuma
data = pd.read_excel('Mall_Customers.xlsx')

# Veri kümesini hazırlama
X =data.iloc[:, 2:].values

# OPTICS algoritması
clustering = OPTICS(min_samples=2, xi=0.05, min_cluster_size=0.1) #min_samples = bir noktanın yoğun bir bölgede kabul edilebilmesi için gereken minimum nokta sayısı  xi=OPTICS algoritmasında küme ayrımı yaparken kullanılan bir eşik değeri min_cluster_size = oluşturulan küme için minimum nokta sayısını belirleyen bir parametre
clustering.fit(X)

# Küme etiketlerini alma
labels = clustering.labels_

# Sonuçları yazdırma
print(labels)