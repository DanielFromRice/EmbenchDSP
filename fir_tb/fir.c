/*
    FIR Helper

    @file fir.c
    @author Eric Torres
    @email edt3@rice.edu
    @date 02/01/2021


    Made at Rice University, Go Owls!

      , _ ,
     ( o o )
    /'` ' `'\
    |'''''''|
    |\\'''//|
       """

*/

#include <stdio.h>
#include "fir.h"

void fir(float* output_array_ptr, float* fir_coefs, int filter_length, int data_amt){


    float padded_in[300] = {0.0};
    padded_in[filter_length] = 1.0;

    for (int i = filter_length; i < data_amt; i++) {
        float sum = 0;
        for (int j = 0; j < filter_length; j++) {
            sum += fir_coefs[j] * padded_in[i - j];
        }
        output_array_ptr[i-filter_length] = sum;
    }
}

int check_if_equal(float* test_data, float* check_data, int data_length, float epsilon){
    int match = 1;
    for (int i = 0; i < data_length; i++) {
        if ((*(test_data + i) < *(check_data + i) - epsilon) || (*(test_data + i) > * (check_data + i) + epsilon)) {
            match = 0;
        }
    }
    return match;    
}