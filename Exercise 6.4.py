str = 'X-DSPAM-Confidence: 0.8475'

colon_index = str.find(':')
float_value = float(str[colon_index+1:])
print(float_value)