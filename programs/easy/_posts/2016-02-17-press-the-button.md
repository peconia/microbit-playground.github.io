---

title: Button Press Message
layout: project

# excerpt for teaser links and Google descriptions
excerpt: "How to use buttons on the micro:bit in Python."

# One -teaser.gif is needed 180 x 110px.
# One -featured.svg is needed. Edit an .SVG from the images directory in a text file and save it with the same name as your program file name.
# File name matches project title eg. 2014-11-29-feature-building-a-score-counter-teaser.png
# Resides in /images/ folder
image:
  feature: 2016-02-17-press-the-button-feature.svg
  teaser:  2016-02-17-press-the-button-teaser.gif

# edit /data/author.yml with your details for info box. Please consider attributing your contribution to inspire kids.
# the author box contains links to twitter/websites etc
author: jez_dean

# Add only if project is updated after publication 2016-12-25
modified:

share: true

comments: yes

---


This program loops forever and waits for a button (or both buttons) to be pressed. When the buttons are pressed, the micro:bit displays a different image.

{% highlight python %}
{% include_relative 2016-02-17-press-the-button.py %}
{% endhighlight %}


### How it Works

#### `while True:` loop

![Conditional loops are intented in Python.]({{ site.baseurl }}/images/2016-02-17-press-the-button-1.gif)

`while True:` is a statement that's always true. Whenever we use it in a Python program it means whatever inside the loop is repeated forever. The line after the statement is indented. This indicates it is inside the loop.  

#### `if` statements

{% highlight python %}
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():   
        microbit.display.show(Image.ANGRY)
    elif microbit.button_a.is_pressed():
        microbit.display.show(Image.HAPPY)
    elif microbit.button_b.is_pressed():
        microbit.display.show(Image.SAD)
{% endhighlight %}
    
Translated into English this is:

{% highlight python %}
If button a is pressed and button b is pressed:
    show angry face
otherwise, if button b is pressed
    show happy face
otherwise if button b is ressed 
    show sad face
{% endhighlight %}

With Python it's really _really_ easy to read the code as English.
    
Indentation is _really_ important when writing Python. Everything after each condition is intended by a `tab` space.
{: .notice-warning}


### Going Further

The micro:bit api lists other images that can be drawn on the display. The `image` class has many attributes:

| Image.HEART | Image.ASLEEP 
| Image.HEART_SMALL | Image.SURPISED |
| Image.HAPPY | Image.SILLY |
| Image.SMILE | Image.FABULOUS |
| Image.SAD | Image.MEH |
| Image.CONFUSED | Image.YES |
| Image.ANGRY | Image.NO |

There is a [full list on the API](http://microbit-micropython.readthedocs.org/en/latest/image.html). Or use the `display` [module](http://microbit-micropython.readthedocs.org/en/latest/display.html) and scroll a message. 