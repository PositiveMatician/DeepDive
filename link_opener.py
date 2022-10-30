import webbrowser as wb
import time
import requests
import threading


def duplicates_remover(list):
    '''Take a list as input 
    Converts it into a dictionary with keys only
    then covert it back to list
    All duplicates gets removed'''
    list = list(dict.fromkeys(list))
    return list






def link_opener(filename,choice_brw):


    #Opening the file 
    with open(filename) as file:
        links = file.readlines()
        print('File opened successfully')
    
    #Browser choosing
    choice_brw = input(f'What browser would you like the links to open in?\n (It will only work if the browser is already installed in device, if you can\'t be bothered choose default)\n1.Chrome\n2.firefox\n3.Safari\n4.default\n')
    brws = ['google-chrome','firefox','safari','windows-default']
    try:
        brw = wb.get(brws[int(choice_brw)-1])
    except Exception as err:
        print(f'{err} <--happened\n')
        print('choosing default\n')
        brw = wb

    #Filtering links_list for duplicate links
    links = duplicates_remover(links)
    print('Duplicate links removed')

    #Iteration through links
    user_input = str()
    def link_opener(link_list):
        '''Takes a list of link and open each link one by one'''
        for p , link in enumerate(link_list):
            try:
                usr = user_input
                #Automatically skips broken links
                print(f'{len(link_list)-p} link/s left\n\n')
                _ = requests.get(link)
                if _.status_code == 404:
                    raise NotImplementedError
                print(f'{link} is opening\nFeel Free to press \'any key\' to advance\n(Trying to advance the link using same key again and again won\'t work, just keep changing the key pressed each time adavanced )')
                brw.open(link)
                for i in range(50):
                    time.sleep(1)
                    if usr!=user_input:
                        print('User input detected\n Moving on to next link\n')
                        break

                        
            except Exception as err:
                print(f'{err} <---happened moving on to the next')
        print('All links have been opened')
        


    #Threading it some good shit!!!
    threading_1 = threading.Thread(target=lambda:link_opener(links))
    threading_1.daemon = True
    threading_1.start()
    while True:
        if threading_1.is_alive():
            exit()
        user_input = input()




    
if __name__ == '__main__':
    file = input('What is the filename and location\n(just provide the file path like C:/user/doc/abc.txt or something)\n\t')
    link_opener(file)









	