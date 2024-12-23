# by:neverfriendme
str = "1234567890123456"
# string to mask
i = "*"
# "*" for masking
print(i * 12+str[12]+str[13]+str[14]+str[15])
# i * 12 because those are the ones we are not going to show.
# then letters 12,13,14,15 because those are the 4 we want to show.
