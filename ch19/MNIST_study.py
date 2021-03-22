from mlxtend.data import loadlocal_mnist
import numpy as np

train_images, train_labels = loadlocal_mnist(
            images_path='MNIST/raw/train-images-idx3-ubyte',
            labels_path='MNIST/raw/train-labels-idx1-ubyte')

train_images = np.reshape(train_images,(60000,28,28))

assert list(np.shape(train_images)) == [60000,28,28]
assert list(np.shape(train_labels)) == [60000]




# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(10,10)
# for i in range(10):
#     for j in range(10):
#         ax[i][j].imshow(train_images[10*i+j],cmap='Greys')
#         ax[i][j].xaxis.set_visible(False)
#         ax[i][j].yaxis.set_visible(False)
# plt.show()


test_images, test_labels = loadlocal_mnist(
            images_path='MNIST/raw/t10k-images-idx3-ubyte',
            labels_path='MNIST/raw/t10k-labels-idx1-ubyte')

test_images = np.reshape(test_images,(10000,28,28))

assert list(np.shape(test_images)) == [10000,28,28]
assert list(np.shape(test_labels)) == [10000]




avg = np.sum(train_images) / 60000 / 28 / 28

train_images = [[(pixel-avg)/256 for row in image for pixel in row]for image in train_images]
test_images = [[(pixel-avg)/256 for row in image for pixel in row]for image in test_images]

import tqdm

def loop(model, images, labels, loss, optimizer):
    correct = 0
    total_loss = 0.0

    with tqdm.trange(len(images)) as t:
        for i in t:
            predicted = model.forward(images[i])
            if np.argmax(predicted)==np.argmax(labels[i]):
                correct += 1
            total_loss += loss.loss(predicted, labels[i])

            if optimizer is not None:
                gradient = loss.gradient(predicted,labels[i])
                model.backward(gradient)
                optimizer.step(model)

            avg_loss = total_loss / (i+1)
            acc = correct / (i+1)
            t.set_description(f"mnist loss: {avg_loss:.3f}acc:{acc:.3f}")



model = np.Linear(784,10)
loss = SoftmaxCrossEntropy()