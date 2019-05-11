# Photo padding script

## The Problem

I had several photos I wanted to get printed online.
They had non-standard aspect ratios.

The vendor I was using would only crop images to make them fit onto the paper.
I wanted to pad the images with whitespace on one edge, to make them fit. So no part of the image would be cut off.

## The solution

So I wrote this script.

Invoke it with `python3 ratio.py file.jpg file2.jpg`.

At the bottom of the script is a list of paper sizes the vendor has.

For each image, this script finds the closest paper size, and pads whichever dimension is required to make the image's aspect ratio fit the paper.

This does not change the resolution. This changes the aspect ratio by only *adding* white pixels.


## Example

Consider [this photo](https://unsplash.com/photos/JZfy4esJjLg) by [Nick Chung](https://unsplash.com/photos/JZfy4esJjLg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

![example.jpg](example.jpg)

Run `python3 ratio.py example.jpg`, then the output `example-padded.jpg` looks like:

![example-padded.jpg](example-padded.jpg)

To change the name of the output file, modify the `newFname` function.


