# Sky Color

Small project to record the color of the sky

I needed realistic sky colors throughout the day to color the background of
[www.codemancer.com](https://www.codemancer.com/) so that it would match the
[real sky color](https://github.com/albertyw/codemancer/issues/29).
There's a lot of [sky colors chosen by designers](http://www.mishistoriasdeterror.com/images/www.materials-world.com/paint-colors/behr/behr-colorsmart/images/behr-colorsmart-28.gif)
and there's some [semi-scientific color calculations](https://academo.org/demos/colour-temperature-relationship/)
but I haven't found a good way of also computing color gradients towards the
horizon (which is affected by local weather).  Being in San Francisco,
I get a fair amount of cloud-free days and a good view of the horizon which
makes this project possible.

## Process

This project will use a camera to take pictures of the daytime sky and calculate
the sky color throughout the day.

1.  Run record.py to take pictures at intervals throughout the day
2.  Save pictures to the photos directory.
3.  Read the photos and find their closest rgb color using compute.py
4.  Write the rgb color for a given time on a given day to output.csv.
