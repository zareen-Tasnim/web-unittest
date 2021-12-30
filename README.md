Automation test scripts for visiting Bongo's Homepage and clicking any of the free content.

In browser.py,
I have taken the url for BongoBd website in init. Then I have created two methods to get the titles and categories of the website. After that I have printed the title and categories by using print function.

In browser_unittest.py,
It is the unittest for browser.py.

Here I have created a list named MAIN_CATEGORIES which includes some of the categories like movies,Tv,Drama. This list doesn't include all the elements of the category as this is dynamic. After that I have created a method named test_main_categories. Here I have compared the list with the categories I have found in get_categories from browser.py. If the category includes the elements of the list ,It will be True.

In same way, test_title method will check if the title I am getting from browser.py's get_title method is same as the title of the website.


In play.py,
In get_random_video method, I have selected a common class for the free contents on bongo site. After that I have created a list with the videos I have found in that class and selected randomly to click.

In get_current_url method, we are getting the url of the clicked video.

After that I have printed it.

In play_unittest.py,
It is the unittest for play.py.

Here I have checked if I am getting the url from the get_current_url method of play.py by using assertTrue function in test_url.


In both of the unittest a html file will be generated in report folder from where we can see if the tests have passed or not.