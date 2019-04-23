########################################
#
# In this module I will be building a single-layer perceptron
# with a constant bias input and a step activation function to
# perform a logical AND function.
#
########################################

import tensorflow as tf

T, F = 1., -1.
bias = 1

# training data consists of the truth table for logical AND for the input
# bias is implemented by adding an extra value of 1 to all examples

train_in = [
    [T, T, bias],
    [T, F, bias],
    [F, T, bias],
    [F, F, bias],
]

# the operations respective results are the output

train_out = [
    [T],
    [F],
    [F],
    [F],
]

w = tf.Variable(tf.random_normal([3, 1]))

#step(x) = { 1 if x >; -1 otherwise}
def step(x):
    is_greater = tf.greater(x, 0)
    as_float = tf.to_float(is_greater)
    doubled = tf.multiply(as_float, 2)
    return tf.subtract(doubled, 1)

output = step(tf.matmul(train_in, w))
error = tf.subtract(train_out, output)
mse = tf.reduce_mean(tf.square(error))

delta = tf.matmul(train_in, error,transpose_a=True)
train = tf.assign(w, tf.add(w, delta))

sess = tf.Session()

sess.run(tf.global_variables_initializer())

err, target = 1, 0
epoch, max_epochs = 0, 10

while err > target and epoch < max_epochs:
    epoch += 1
    err, _ = sess.run([mse, train])
    print ('epoch:', epoch, '\nmse: ', err)

writer = tf.summary.FileWriter