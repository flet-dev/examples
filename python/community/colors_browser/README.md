# Flet-Color-Browser

![GitHub top language](https://img.shields.io/github/languages/top/ndonkoHenri/Flet-Color-Browser)
![GitHub language count](https://img.shields.io/github/languages/count/ndonkoHenri/Flet-Color-Browser)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/ndonkoHenri/Flet-Color-Browser?color=ry)

> _From my experience, working with colors is not that easy._
## Table of contents:
- [Introduction](#what-is-this-about-introduction)
- [Source of Inspiration](#source-of-inspiration)
- [Screen captures](#screen-captures)
- [How to get started?](#how-to-get-started)
- [How to deploy to Fly.io?](#how-to-deploy-to-flyio)
- [Issues/Contribution](#issuescontribution)


### What is this about? (Introduction)

 A simple but sophisticated tool(Web and desktop UI) for easy color selection when developing [Flet](https://flet.dev/) applications.
Here is a link to the online/web version of this tool -> <u>[flet-colors-browser.fly.dev](https://flet-colors-browser.fly.dev/)</u>

### Source of Inspiration

I decided to build up this tool after looking at the [Flet-Icons-Browser](https://github.com/flet-dev/examples/tree/main/python/apps/icons-browser) - a simple browser which eases Icon selection when developing Flet apps . 
This tool is actually a refactored-clone(or fork if you want) of it. 
I just added my personal UI touch and included more comments in the code :) 

### Screen captures
This tool has two versions: One using a [GridView](https://flet.dev/docs/controls/gridview) to display the colors, and another using a [ListView](https://flet.dev/docs/controls/listview) in [Tabs](https://flet.dev/docs/controls/tabs). 

Below are some captures I made of the tool in execution.

- _**Version 1:**_
  - _Dark Mode_
        <br><br>
      ![V1 Dark Mode](https://user-images.githubusercontent.com/98978078/193250212-a56477ac-f063-4b45-99e3-7dbb971eee27.JPG)
        <br><br>
  - _Light Mode_
        <br><br>
        ![V1 Light Mode](https://user-images.githubusercontent.com/98978078/193256037-2ee24033-425f-4c9e-958a-f20e3c207917.JPG)
      

- _**Version 2:**_
  - _Dark Mode_
       <br><br>
      ![V2 Light Mode](https://user-images.githubusercontent.com/98978078/193249865-b626c155-7dc3-4188-9fc7-e7a163357c5d.JPG)

       <br><br>
    - _Light Mode_
         <br><br>
      ![Capture](https://user-images.githubusercontent.com/98978078/193256644-3cf3dec8-ca52-4a6e-a772-f567074891f5.JPG)
    <br><br>
  - **GIF Video**
        <br><br>
        ![Colors-Browser GIF](https://user-images.githubusercontent.com/98978078/193254404-bef6c113-b71d-4e01-b732-cd5d268619ec.gif)
  
### How to get started?

**Easiest Way:** You can [open it on your browser](https://flet-colors-browser.fly.dev/) and install it as a PWA(Progressive Web Application). It would then be found on your desktop(Windows, macOS, Linux.. etc), and you could run it any time. Follow the guide below gotten from a [Post on Medium](https://medium.com/@dhormale/install-pwa-on-windows-desktop-via-google-chrome-browser-6907c01eebe4).

![How to Install as PWA](https://miro.medium.com/max/720/1*BQ5FlcpuLTOBfF5vLvv6Bg.gif)

**Second-Easiest Way:** You can just download an archive(for Windows, macOS and Linux only) from the [releases](https://github.com/ndonkoHenri/Flet-Color-Browser/releases) section, extract this and run the standalone executable file(~25Mo) found in it.


**Hardest Way:**
- Start by cloning and unzipping this repo: [how-to](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- Enter the directory

        cd Flet-Color-Browser
- Install the requirements(only Flet is required):
    `pip install flet`
- Run the `main.py` file

      python main.py

### How to deploy to Fly.io?

A detailed version of how to deploy [Flet](https://github.com/flet-dev/flet) apps on [Fly.io](https://fly.io/) could be found <u>[here](https://flet.dev/docs/guides/python/deploying-web-app/fly-io)</u>.

Deploy:

    flyctl deploy

Check deployment:

    flyctl status

Re-deploy:

    flyctl deploy --no-cache


### Issues/Contribution
I tried my best to make this project simple and easy to understand, but if you have problems/issues while using this :(, 
then you are free to raise an issue and I will happily respond.

If you instead want to contribute(new features, bug/typo fixes, etc), just fork this project and make a pull request. :)
