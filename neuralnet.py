#CET313 Codie Heaney - bh97rt

from Matrix import Matrix
import numpy as np
import random

#sigmoid used as activation function for each neuron
def sigmoid_activation(result):
    return 1 / (1 + np.exp(-result))

#sigmoid derivative used for backpropogation
def sigmoid_activation_d(result):
    return result * (1 - result)

class NN:

    #create a neural network with a set of input, hidden, and output neurons
    #Learning rate is set by default to 0.1 but can be changed at creation if an additional float is added when constructing
    def __init__(self, inputs, hidden, outputs, learning_rate = 0.1):
        self.input_neurons = inputs
        self.hidden_neurons = hidden
        self.output_neurons = outputs
        
        self.hidden_weight = Matrix(self.hidden_neurons, self.input_neurons)
        self.output_weight = Matrix(self.output_neurons, self.hidden_neurons)

        #sets weight values
        self.hidden_weight.randomise()
        self.output_weight.randomise()
        
        
        self.hidden_bias = Matrix(self.hidden_neurons, 1)
        self.output_bias = Matrix(self.output_neurons, 1)

        #sets bias values
        self.hidden_bias.randomise()
        self.output_bias.randomise()
        
        self.learning_rate = learning_rate

    #function for calculating gradient descent using sigmoid derivative
    def gradient(self, matrix, error):
        gradient = Matrix.map_func_return(matrix, sigmoid_activation_d)
        gradient.multiply(error)
        gradient.multiply(self.learning_rate)
        return gradient

    #function for calculating bias deltas based on gradient
    def deltas(self, matrix, gradient):
        matrix_transpose = Matrix.transpose_return(matrix)
        deltas = Matrix.multiply_return(gradient, matrix_transpose)
        return deltas

    #feedforward function pushes inputs through the neural network and returns an output
    def feedforward(self, inputs):

        #if the input is already a matrix it doesn't require conversion
        if((isinstance(inputs, Matrix))):
            input_matrix = inputs
        else:
            input_matrix = Matrix.fromArray_return(inputs)
        
        #sigmoid(SUM(inputs * weights) + bias)
        #hidden layer calculation
        hidden_feed = Matrix.multiply_return(self.hidden_weight, input_matrix)
        hidden_feed.add(self.hidden_bias)
        hidden_feed.map_func(sigmoid_activation)

        #output layer calculation
        output_feed = Matrix.multiply_return(self.output_weight, hidden_feed)
        output_feed.add(self.output_bias)
        output_feed.map_func(sigmoid_activation)

        #[0] = outputs [1] = outputs from hidden layer [2] = outputs in matrix form
        return [output_feed.toArray(), hidden_feed, output_feed]
    
    def backpropagation(self, inputs, targets):
        results = self.feedforward(inputs)
        
        #Calculate output error against the target
        target_matrix = Matrix.fromArray_return(targets)
        output_error = Matrix.subtract_return(target_matrix, results[2])
        #print("\nTraining Error (Target - Output)")
        #output_error.show()
        
        #calculate output weights gradient descent
        output_grad = self.gradient(results[2], output_error)
        
        #calculate weight deltas
        output_deltas = self.deltas(results[1], output_grad)
        
        #adjust output weights and bias
        self.output_weight.add(output_deltas)
        self.output_bias.add(output_grad)
        
        #calculate hidden errors
        hidden_weight_trans = Matrix.transpose_return(self.output_weight)
        hidden_error = Matrix.multiply_return(hidden_weight_trans, output_error)
        
        #calculate hidden weights gradient descent
        hidden_grad = self.gradient(results[1], hidden_error)
        
        #calculate hidden deltas
        hidden_deltas = self.deltas(Matrix.fromArray_return(inputs), hidden_grad)
        
        #adjust input errors
        self.hidden_weight.add(hidden_deltas)
        self.hidden_bias.add(hidden_grad)
