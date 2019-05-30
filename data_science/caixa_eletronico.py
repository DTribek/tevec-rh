class ATM():
    """
    ... Develop our code ...
    """

    def process_request(self, input):

        money_value = int(input['request']['request'])

        n50=0
        n20=0
        n50 = money_value // 50
        response_dict = {}
        final = {}

        #Check if the requested amount can be maximized with 50 values
        if ( money_value - n50*50) % 20 == 0: 
            n20 = (money_value -n50*50) // 20
            response_dict['20'] = n20
            response_dict['50'] = n50
        #Check if the requested value can be reached completing with 20's
        elif (money_value - (n50-1)*50) % 20 == 0:
            n50 = n50 -1
            n20 = (money_value -n50*50) // 20
            response_dict['20'] = n20
            response_dict['50'] = n50
        #Value not compatible
        else:
            response_dict['error'] = 'Sua mensagem de erro'

        response = {}
        response['response'] = response_dict
        
        input['requester'] = input.pop('request')
        input['requester']['requested'] = input['requester'].pop('request')
        final = dict(input)
        final.update(response)

        return final


if __name__ == "__main__":

    import json

    # Loads the test file
    input_file = open("caixa_eletronico_amostras_teste.json")
    test_samples = json.load(input_file)

    # Instance proposed class
    atm = ATM()

    # Loops every test sample
    count_success, count_fail = 0, 0
    for idx, sample in enumerate(test_samples):
        input    = sample.get("input")
        correct_output = sample.get("output")
        processed_output = atm.process_request(input)
        
        # Checks if the result is correct
        if processed_output == correct_output:
            count_success += 1
            print("Sample # {} - Success".format(idx))
        # 
        else:
            print("Sample # {} - Error".format(idx))
            count_fail += 1
    
    print("You got {} right answers and {} wrong answers".format(count_success, count_fail))
        

