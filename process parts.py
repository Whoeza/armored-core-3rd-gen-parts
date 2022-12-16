import re
##
# input and output files
##
# ac3 early gen
# input: './data/input/ac3 3 SL parts names list.txt' and
# output: './data/output/ac3-3-sl-parts.txt'
##
# ac3 later gen
# input: './data/input/ac3 NB LR parts names list.txt' and
# output: './data/output/ac3-3-nr-lr-parts.txt'
##
input_filename = './data/input/ac3 NB LR parts names list.txt'
output_filename = './data/output/ac3-3-nb-lr-parts.txt'
##
# these regexps match the parts and the section names
##
re_section = '^==([\w ]+)==$'
re_part_name = '^\! \[\[([\+ \.\|\/\-\w]+)\]\]$'
re_part_name_v2 = '^(\! \[\[(^\]\])+\]\])$'  # test it
##
# make a full regexp to match either one of the two
##
full_re = '(' + re_section + '|' + re_part_name + ')'
##
# compile regexps from strings to Pattern objects
##
compiled_re_section = re.compile(re_section)
compiled_re_part_name = re.compile(re_part_name)
compiled_full_re = re.compile(full_re)
##
# output string result
##
output_parts_list = ""
##
# read the wiki file and save sections and parts names
##
with open(input_filename, 'r') as input_file:
    for line in input_file:
        is_matching = re.match(compiled_full_re, line)
        section_name = re.findall(compiled_re_section, line)
        part_name = re.findall(compiled_re_part_name, line)
        if section_name:
            # print("Section: %s" % section_name)
            # print(section_name, section_name[0][0])  # DEBUG
            output_parts_list += '\n' + "Section: " + section_name[0]+ '\n'
        elif part_name:
            # print(" + part name: %s" % part_name)
            # output_parts_list += " + part name: " + part_name[0] + '\n'
            output_parts_list += part_name[0] + '\n'
        # else:
            # print("skip line: %s" % line)

        # do for loop stuff

##
# print the result and write it to disk
##
print(output_parts_list)
with open(output_filename, 'w') as output_file:
    output_file.write(output_parts_list)
