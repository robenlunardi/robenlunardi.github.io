# bib2yaml.py
import re
import sys
 
# from terminal arguments
str_input = sys.argv[1]
str_output = sys.argv[2]
 
# open the file
with open(str_input, 'r') as fr:
    list_lines = fr.readlines()
 
# list the output line
list_output = []

# string in publist.yml
stringTitle = ''
stringAuthors = ''
stringUrl = ''
stringImage ='' 
stringDisplay =''
stringYear =''
stringDoi = ''
stringCode= ''
stringAbstract=''
# each string correspond to one line in publist.yml, complete (except title):
stringComplete =''
booktitle = '' # (confname/journalname)
volume = ''
issue= '' 
pages = ''
publisher = ''

# go through the lines
for str_line in list_lines:
     
    # first line with id
    if str_line.startswith('@'):
        # sg_t1 = re.search('^@(.*){(.*),', str_line)
        sg_t1 = re.search('^@(.*){(.*),', str_line)
        str_id = re.sub(':','',sg_t1.group(2))
        str_first = '\n-%s: &%s' % (sg_t1.group(1), str_id)
        # list_output.append(str_first)
        # list_output.append(list_output_demaiscampos)
        if(stringComplete != ''):
            # mount stringDisplay with the fields
            if booktitle !='':
                stringDisplay = booktitle
                booktitle=''
            if volume != '':
                if issue != '':
                    stringDisplay = stringDisplay + ', '+volume +'(' + issue + '), '
                    volume =''
                    issue = ''
                else:
                    stringDisplay = stringDisplay + ', '+ volume
                    volume =''
            if pages != '':
                stringDisplay = stringDisplay+ ', '+pages
                pages = ''
            if publisher != '': 
                stringDisplay = stringDisplay+ '. '+publisher                 
            
            # mount complete string
            stringComplete = stringComplete+stringTitle+'\n'+stringAuthors
            stringTitle = ''
            stringAuthors = ''
            if stringUrl != '': 
                stringComplete = stringComplete+'\n'+stringUrl
                stringUrl = ''
            if stringDisplay != '': 
                stringDisplay = '  display: "'+stringDisplay+'".'
                stringComplete = stringComplete+'\n'+stringDisplay
                stringDisplay = ''
            if stringYear != '': 
                stringComplete = stringComplete+'\n'+stringYear
                stringYear = '' 
            if stringDoi != '': 
                stringComplete = stringComplete+'\n'+stringDoi
                stringDoi = ''    
            if stringAbstract != '': 
                stringComplete = stringComplete+'\n'+stringAbstract
                stringAbstract = ''
            list_output.append(stringComplete+'\n')
            stringComplete = ''
        # list_output_demaiscampos = []
        print(str_first)
 
    # for the other lines
    # elif str_line.startswith('\t'):
    elif str_line.startswith("  "):
        print ("dentro do elsif")
        # sg_tn = re.search('^\t(.*) = {(.*?)}', str_line)
        sg_tn = re.search('^  (.*) = {(.*?)}', str_line)
        print(str_line)
        str_cat = sg_tn.group(1).lower()
        str_val = sg_tn.group(2)

        # if str_cat=="title":
        #     str_gen_out = '  %s: "%s"' % (str_cat, str_val)
        #     list_output.append(str_gen_out)
 
        # make a list of all the authors
        if str_cat== 'title':
            # str_gen_out = '- %s: "%s"' % (str_cat, str_val)
            str_gen_out = '%s: "%s"' % (str_cat, str_val)
            stringComplete = '- '
            stringTitle = str_gen_out
            # list_output.append(str_gen_out)

        elif str_cat=='author':
            list_authors = str_val.split(' and ')
            # str_auths = '\n    -'.join(list_authors)
            str_auths = ', '.join(list_authors)
            # str_aut_out = '  %s:\n    -%s' % (str_cat, str_auths)
            str_aut_out = '  %ss: %s' % (str_cat, str_auths)
            print(str_auths)
            print("antes do append")
            # list_output.append(str_aut_out)
            stringAuthors=str_aut_out
      
        elif str_cat=='doi':
            str_gen_out = '  %s: "%s"' % (str_cat, str_val)
            # list_output.append(str_gen_out)
            stringDoi=str_gen_out

        elif str_cat=='url':
            str_gen_out = '  %s: "%s"' % (str_cat, str_val)
            # list_output.append(str_gen_out)
            stringUrl=str_gen_out
       
        elif str_cat=='abstract':
            str_gen_out = '  %s: "%s"' % (str_cat, str_val)
            # list_output.append(str_gen_out)
            stringAbstract=str_gen_out
            
        elif str_cat == 'year':
            str_jt_out = '  %s: %s' % (str_cat, str_val)
            # list_output.append(str_jt_out)
            stringYear=str_jt_out

        #display: booktitle, volume(issue), pages. publisher.  
        elif str_cat == 'booktitle':
            booktitle = '%s' % (str_val)
        elif str_cat == 'volume':
            volume = '%s' % (str_val)
        elif str_cat == 'issue':
            issue = '%s' % (str_val)
        elif str_cat == 'pages':
            pages = '%s' % (str_val)
        elif str_cat == 'publisher':
            publisher = '%s' % (str_val)            
        else:
            print('not mapped category ' + str_cat)
            
        # else:
        #     # all the integer values
        #     list_ints = ['number','volume','read','year']
        #     if str_cat in list_ints:
        #         str_jt_out = '  %s: %s' % (str_cat, str_val)
        #         # list_output.append(str_jt_out)
        #         if(stringComplete==''):
        #             stringComplete=str_jt_out
        #         else:
        #             stringComplete=stringComplete+'\n'+str_jt_out 
                 
        #     # all the string values
        #     else:
        #         str_gen_out = '  %s: "%s"' % (str_cat, str_val)
        #         # list_output.append(str_gen_out)
        #         if(stringComplete==''):
        #             stringComplete=str_gen_out
        #         else:
        #             stringComplete=stringComplete+'\n'+str_gen_out 

# for the last reference
if booktitle !='':
    stringDisplay = booktitle
    booktitle=''
if volume != '':
    if issue != '':
        stringDisplay = stringDisplay + ', '+volume +'(' + issue + '), '
        volume =''
        issue = ''
    else:
        stringDisplay = stringDisplay + ', '+ volume
        volume =''
if pages != '':
    stringDisplay = stringDisplay+ ', '+pages
    pages = ''
if publisher != '': 
    stringDisplay = stringDisplay+ '. '+publisher                    

# mount complete string
stringComplete = stringComplete+stringTitle+'\n'+stringAuthors
stringTitle = ''
stringAuthors = ''
if stringUrl != '': 
    stringComplete = stringComplete+'\n'+stringUrl
    stringUrl = ''
if stringDisplay != '': 
    stringDisplay = '  display: "'+stringDisplay+'."'
    stringComplete = stringComplete+'\n'+stringDisplay
    stringDisplay = ''
if stringYear != '': 
    stringComplete = stringComplete+'\n'+stringYear
    stringYear = '' 
if stringDoi != '': 
    stringComplete = stringComplete+'\n'+stringDoi
    stringDoi = ''    
if stringAbstract != '': 
    stringComplete = stringComplete+'\n'+stringAbstract
    stringAbstract = ''
list_output.append(stringComplete+'\n')

with open(str_output,'w') as fw:
    fw.write('\n'.join(list_output))
