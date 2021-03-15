--[[ H**********************************************************************
* FILENAME: OTP.lua
*
* DESCRIPTION: Program that implements a simple One Time Pad algorithm given
*              an input string.
*
* FUNCTIONS: OTP()
*
* AUTHOR: Carlos Garcia, Daniela Vignau, Hector Reyes
*
*H* --]]

AlphabetLength = 26
HelperText = {"Input Text", "Key", "Ciphered"} -- For formatting purposes
function OTP(input_string)
    local otp_keys= {} -- Will contain every key value, stored in a column-based system
    for i = 1, #input_string do
        local c = input_string:sub(i,i)
        -- Store every input char byte value in the array
        otp_keys[i-1] = string.byte(c) - 65

        local rand_index = math.random(0,AlphabetLength-1)
        -- Store every randomly generated value in the array
        otp_keys[(i-1)+string.len(input_string)] = rand_index

        local sumation = otp_keys[i-1] + otp_keys[(i-1)+string.len(input_string)]
        -- Check for exceding values
        if sumation >= AlphabetLength
            then
            sumation = sumation - AlphabetLength
        end
        -- Store every added value in the array
        otp_keys[i-1 + (2* string.len(input_string))] = sumation
    end

    -- Print results
    for j = 1, 3 do
        print(HelperText[j])
        for i = 1, #input_string do
            io.write(string.char(otp_keys[(i-1) + (#input_string* (j-1))]+65), '(', otp_keys[(i-1) + (#input_string* (j-1))], ') ')
        end
        print("\n------------------------------------------------\n")

    end


end

io.write("Please enter a string to encript... ")
local user_input = io.read()
local uppercase = user_input:upper() -- To standardize the input
OTP(uppercase);
