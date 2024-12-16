import tensorflow as tf

tensor1 = tf.Variable([["Test","OK"],["Hehe","AHHH"]])
#print(tensor1.shape)

t = tf.zeros([2,1,2]) #2 lists that contains 1 lists that contains 2 0's 
print(t)

t = tf.reshape(t, [4,1])
print(t)