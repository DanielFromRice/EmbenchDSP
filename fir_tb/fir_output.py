import numpy as np

filter_coefs = [2.1804394561215686e-06, 7.307213539159978e-06, -3.827449953166632e-06, -1.4704540164019638e-05, 3.3367975113573343e-07, 2.8159131092762438e-05, 1.1167249741906437e-05, -4.416534273865827e-05, -3.661105503672574e-05, 5.733435304013607e-05, 8.078317610919384e-05, -5.763052084539841e-05, -0.0001453858201804361, 3.0666856104380794e-05, 0.0002258620282978998, 4.056900826626298e-05, -0.00030831882944288896, -0.00017203222519024828, 0.0003674277018298899, 0.00037300120240838105, -0.00036651161331593854, -0.0006392079118629813, 0.00026082827462677586, 0.0009459340394524694, -4.714989220599039e-06, -0.0012428881934381962, -0.0004375037249085257, 0.0014528732430846628, 0.0010778933037575956, -0.0014761146027485246, -0.0018906274832902327, 0.001201438616970056, 0.002799916832082243, -0.0005243490768165171, -0.0036733848501805328, -0.0006293437919894823, 0.004323894493194634, 0.002277193333147555, -0.004521857372400284, -0.004355041875733149, 0.004018432361160899, 0.006697649371843505, -0.002577981761373245, -0.009028932733824867, 1.6049239798177332e-05, 0.010964016532447503, 0.003762616934983964, -0.012022173026535866, -0.00873241393718241, 0.011644736846185128, 0.014727897127973032, -0.009203865740471018, -0.021442350947156043, 0.0039711052879326724, 0.028446433474786453, 0.005030229352636568, -0.035226192854648196, -0.019520876613283798, 0.04123651346991793, 0.043757133709014025, -0.04596309477471016, -0.09358118837624176, 0.048984251977186796, 0.31403596892799635, 0.44997659139669505, 0.31403596892799635, 0.048984251977186796, -0.09358118837624176, -0.04596309477471016, 0.043757133709014025, 0.04123651346991793, -0.019520876613283798, -0.035226192854648196, 0.005030229352636568, 0.028446433474786453, 0.0039711052879326724, -0.021442350947156043, -0.009203865740471018, 0.014727897127973032, 0.011644736846185128, -0.00873241393718241, -0.012022173026535866, 0.003762616934983964, 0.010964016532447503, 1.6049239798177332e-05, -0.009028932733824867, -0.002577981761373245, 0.006697649371843505, 0.004018432361160899, -0.004355041875733149, -0.004521857372400284, 0.002277193333147555, 0.004323894493194634, -0.0006293437919894823, -0.0036733848501805328, -0.0005243490768165171, 0.002799916832082243, 0.001201438616970056, -0.0018906274832902327, -0.0014761146027485246, 0.0010778933037575956, 0.0014528732430846628, -0.0004375037249085257, -0.0012428881934381962, -4.714989220599039e-06, 0.0009459340394524694, 0.00026082827462677586, -0.0006392079118629813, -0.00036651161331593854, 0.00037300120240838105, 0.0003674277018298899, -0.00017203222519024828, -0.00030831882944288896, 4.056900826626298e-05, 0.0002258620282978998, 3.0666856104380794e-05, -0.0001453858201804361, -5.763052084539841e-05, 8.078317610919384e-05, 5.733435304013607e-05, -3.661105503672574e-05, -4.416534273865827e-05, 1.1167249741906437e-05, 2.8159131092762438e-05, 3.3367975113573343e-07, -1.4704540164019638e-05, -3.827449953166632e-06, 7.307213539159978e-06, 2.1804394561215686e-06]
filter_length = len(filter_coefs)

data = np.zeros(300)

padded_data = np.zeros(len(data) + filter_length)
padded_data[filter_length] = 1.0

output_data = np.copy(padded_data)

for i in range(filter_length, len(padded_data)):
    sum = 0
    for j in range(filter_length):
        sum += filter_coefs[j] * padded_data[i - j]
    output_data[i] = sum

output_data = output_data[filter_length:]
str_out = ""
for num in output_data:
    str_out += str(num) + ", "

str_out = str_out[:-2]
print(str_out)