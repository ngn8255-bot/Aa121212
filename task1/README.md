This is a tiny Python project for library sign-up. It’s a basic tool to check if user information is valid. I built a  Library  class with four key methods:
 -  enroll_library() : Asks for your name. It can’t be empty, the first character can’t be a number, and all letters after the first must be lowercase. It keeps asking until you enter a valid name.
-  _sex_() : Asks for your sex, only accepting “male” or “female”. Invalid inputs will trigger a re-prompt.
-  _year_() : Asks for your academic year (1-4). It checks for valid numbers and re-prompts if you enter something wrong.
-  complete_registration() : Checks if all info is filled. If yes, it shows your details and says registration is done; if not, it tells you registration failed.
 The methods work step by step: start with  enroll_library() , then it automatically calls  _sex_()  and  _year_() . Finally, run  complete_registration()  to finish.
 It’s simple, but it helped me practice splitting code into files, using class methods, and validating user inputs.
