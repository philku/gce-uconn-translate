# Google Translate API Example

## The Application

### Files
This application uses the following main file structure:

gce-uconn-translate                         <br>
├─ requirements.txt                       <br>
├─ app.yaml                               <br>
├─ main.py                                <br>
├─ templates                                <br>
│  ├── index.html

#### requirements.txt
A list of the required packages for the app

#### app.yaml
A config file for google app engine

#### main.py
The main application

#### templates
HTML used in the app. Only one page is used.

### 

## Lab

### 1
Create a new project (if needed)
![photo 1](https://raw.githubusercontent.com/philku/gce-uconn-translate/master/readme_pictures/1.JPG)

### 2
Enable the Cloud Translation API

In the search box at the top of your Google Cloud Console, type in "translate" and select "Cloud Translation API".
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/2.png)

On the Cloud Translation API page, click Enable.
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/3.png)

### 3
Download and Deploy the Site

#### 3.a
Start Google Cloud Shell by clicking the cloud shell icon on the top right of your screen.
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/4.png)

#### 3.b
Create a Project Folder

```
mkdir translate
```

#### 3.c
Enter the Project Folder

```
cd translate
```

#### 3.c
Pull the project

```
git clone https://github.com/philku/gce-uconn-translate.git .
```

#### 3.c
Deploy the project

```
gcloud app deploy
```

You may be asked to select a region for your app. Choose the region closest to you.
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/5.png)

You will be verify the details of the deployment. Hit enter.
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/6.png)

#### 3.e
Open the site by typing:

```
gcloud app browse
```

This should open your site in a new window. If it does not, click on the link.
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/7.png)

#### 3.f
You should now be at the site
![](https://github.com/philku/gce-uconn-translate/blob/master/readme_pictures/8.png)