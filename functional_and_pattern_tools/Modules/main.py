#with an import like this we need to put the module1 prefix because we imported the functions inside, inside the namespace module1 not to this "file" namespace
import module_1
from module_2 import print_age_in_portuguese
from module_2 import page_break
module_1.print_name("abilio")
module_1.print_name_in_portuguese("abilio")

page_break()

from module_3 import module_3 as module_file
import module_3.module_3 as whole_folder # import module_3 as whole_folder would be useless as couldnt use like whole_package.hello.hello_en.print_hello_en() like bellow, because __init__.py is missing
#so i need to import the submodule directly here
module_file.print_module_3()
whole_folder.print_module_3()

page_break()


print_age_in_portuguese('26')
print(locals())

page_break()

print(dir(module_1))
print(dir(print_age_in_portuguese))

page_break()
#using whats in the __init__.py (only putted the english ones)
import package_prints as whole_package
from package_prints import fl_en, gb_en, hello_en as direct_function_h # the ones before the last are ignored
from package_prints import gb_en as direct_functions_g
from package_prints import fl_en as direct_functions_fl
whole_package.hello.hello_en.print_hello_en() # cant do it with the jp, because these where not included in the __init__ file
whole_package.hello_en.print_hello_en() # cant do it with the jp, because these where not included in the __init__ file
direct_functions_g.print_gb_en() # same as above + dont need to tell which "folder+file" can do the cuntion directly
page_break()
#importing others i need to be specific
from package_prints.hello import hello_jp
hello_jp.print_hello_jp()
