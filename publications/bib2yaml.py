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
stringDemaisCampos =''
 
# go through the lines
for str_line in list_lines:
     
    # first line with id
    if str_line.startswith('@'):
        # sg_t1 = re.search('^@(.*){(.*),', str_line)
        sg_t1 = re.search('^@(.*){(.*),', str_line)
        print (sg_t1)
        print ("passei aqui ")
        str_id = re.sub(':','',sg_t1.group(2))
        str_first = '\n-%s: &%s' % (sg_t1.group(1), str_id)
        # list_output.append(str_first)
        # list_output.append(list_output_demaiscampos)
        if(stringDemaisCampos != ''):
            list_output.append(stringDemaisCampos+'\n')
            stringDemaisCampos = ''
        # list_output_demaiscampos = []
        print(str_first)
 
    # for the other lines
    # elif str_line.startswith('\t'):
    elif str_line.startswith("  "):
        print ("dentro do elsif")
        # sg_tn = re.search('^\t(.*) = {(.*?)}', str_line)
        sg_tn = re.search('^  (.*) = {(.*?)}', str_line)
        print ("dentro do elsif")
        print(str_line)
        str_cat = sg_tn.group(1).lower()
        str_val = sg_tn.group(2)

        # if str_cat=="title":
        #     str_gen_out = '  %s: "%s"' % (str_cat, str_val)
        #     list_output.append(str_gen_out)
 
        # make a list of all the authors
        if str_cat== 'title':
            str_gen_out = '- %s: "%s"' % (str_cat, str_val)
            list_output.append(str_gen_out)

        elif str_cat=='author':
            list_authors = str_val.split(' and ')
            # str_auths = '\n    -'.join(list_authors)
            str_auths = ', '.join(list_authors)
            # str_aut_out = '  %s:\n    -%s' % (str_cat, str_auths)
            str_aut_out = '  %s: %s' % (str_cat, str_auths)
            print(str_auths)
            print("antes do append")
            # list_output.append(str_aut_out)
            if(stringDemaisCampos==''):
                stringDemaisCampos=str_aut_out
            else:
                stringDemaisCampos=stringDemaisCampos+'\n'+str_aut_out 

        else:
            # all the integer values
            list_ints = ['number','volume','read','year']
            if str_cat in list_ints:
                str_jt_out = '  %s: %s' % (str_cat, str_val)
                # list_output.append(str_jt_out)
                if(stringDemaisCampos==''):
                    stringDemaisCampos=str_jt_out
                else:
                    stringDemaisCampos=stringDemaisCampos+'\n'+str_jt_out 
                 
            # all the string values
            else:
                str_gen_out = '  %s: "%s"' % (str_cat, str_val)
                # list_output.append(str_gen_out)
                if(stringDemaisCampos==''):
                    stringDemaisCampos=str_gen_out
                else:
                    stringDemaisCampos=stringDemaisCampos+'\n'+str_gen_out 
list_output.append(stringDemaisCampos) 
with open(str_output,'w') as fw:
    fw.write('\n'.join(list_output))
