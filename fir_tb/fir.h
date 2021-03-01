/*
    Header file for FIR Filter

    @file fir.h
    @author Eric Torres
    @email edt3@rice.edu
    @date 6 Feb 2021

    Made at Rice University, Go Owls!

      , _ ,
     ( o o )
    /'` ' `'\
    |'''''''|
    |\\'''//|
       """

*/

#ifndef FIR_H
#define FIR_H

/*
 * FIR Filter
 * 
 * Params:
 *      Stuff
 *      kjidjf
 * 
 * 
*/

void fir(float* output_array_ptr, float* fir_coefs, int filter_length, int data_amt);

int check_if_equal(float* test_data, float* check_data, int data_length, float epsilon);

#endif