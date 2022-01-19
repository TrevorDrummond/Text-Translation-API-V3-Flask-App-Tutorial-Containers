# Build a Flask app with Azure Cognitive Services Containers
>Repository Forked from - [tutorial: Build a Flask app with Azure Cognitive Services](https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Flask-App-Tutorial)

With this sample, you'll build a Flask web app that uses Azure Cognitive Service containers to translate text. If you run into any issues, let us know by submitting and issue.

## What is Flask?

Flask is a microframework for creating web applications. This means Flask provides you with tools, libraries, and technologies that allow you to build a web application. This web application can be some web pages, a blog, a wiki or go as substantive as a web-based calendar application or a commercial website.

For those of you who want to deep dive after this tutorial here are a few helpful links:

* [Flask documentation](http://flask.pocoo.org/)
* [Flask for Dummies - A Beginner's Guide to Flask](https://codeburst.io/flask-for-dummies-a-beginners-guide-to-flask-part-uno-53aec6afc5b1)


## What are Azure Cognitive Services containers?
[Azure Cognitive Services Containers Overview](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-container-support)

## Prerequisites

Let's review the software and subscription keys that you'll need for this tutorial.

* [Python 3.5.2 or later](https://www.python.org/downloads/)
* [Git tools](https://git-scm.com/downloads)
* An IDE or text editor, such as [Visual Studio Code](https://code.visualstudio.com/) or [Atom](https://atom.io/)  
* [Chrome](https://www.google.com/chrome/browser/) or [Firefox](https://www.mozilla.org/firefox)
* A **Language Detection** container running in your environment.
* A **Language Translator** container running in your environment.

## Register for the gated preview
Access to the Language Translator container requires approval. Request approval via this link:
[Application for Translator (standard) container](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR1160WOYu0dAjKAuCahR9pRUNzVLRDdUMUNYMlkwVlREQkJPN01PN0haUSQlQCN0PWcu)

## Create an account and subscribe to resources

You're going to need two subscription keys for this tutorial. This means that you need to create a resource within your Azure account for:

* Translator Text
* Text Analytics

Use [Create a Cognitive Services Account in the Azure portal](https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account) for step-by-step instructions to create resources.

**IMPORTANT NOTE**: Cognitive services endpoints will be used for metering and translation model downloads only. 

## Pull the latest container images for detect and translate
```
docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/language
```
```
docker pull mcr.microsoft.com/azure-cognitive-services/translator/text-translation
```

## Start the containers in your environment
Follow the guides below to setup local containers for:

* [Language detection](https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/language-detection/how-to/use-containers)

* [Translator](https://docs.microsoft.com/en-us/Azure/cognitive-services/translator/containers/translator-how-to-install-container#:~:text=%20Install%20and%20run%20Translator%20containers%20%28preview%29%20,and%20recommended...%205%20Next%20steps.%20%20More%20)


## Clone the sample

This is pretty straightforward, clone this repository:

```
git clone https://github.com/TrevorDrummond/Text-Translation-API-V3-Flask-App-Tutorial-Containers.git
```

## Create and activate your virtual environment with `virtualenv`

Let's create a virtual environment for our Flask app using `virtualenv`. Using a virtual environment ensures that you have a clean environment to work from.

1. In your working directory (where you cloned the repo), run this command to create a virtual environment:
   **macOS/Linux:**
   ```
   virtualenv venv --python=python3
   ```
   We've explicitly declared that the virtual environment should use Python 3. This ensures that users with multiple Python installations are using the correct version.

   **Windows CMD / Windows Bash:**
   ```
   virtualenv venv
   ```
   To keep things simple, we're naming your virtual environment venv.

2. The commands to activate your virtual environment will vary depending on your platform/shell:   

   | Platform | Shell | Command |
   |----------|-------|---------|
   | macOS/Linux | bash/zsh | `source venv/bin/activate` |
   | Windows | bash | `source venv/Scripts/activate` |
   | | Command Line | `venv\Scripts\activate.bat` |
   | | PowerShell | `venv\Scripts\Activate.ps1` |

   After running this command, your command line or terminal session should be prefaced with `venv`.

3. You can deactivate the session at any time by typing this into the command line or terminal: `deactivate`.

**NOTE**: Python has extensive documentation for creating and managing virtual environments, see [virtualenv](https://virtualenv.pypa.io/en/latest/).

## Install `requests`

Requests is a popular module that is used to send HTTP 1.1 requests. There’s no need to manually add query strings to your URLs, or to form-encode your POST data.

1. To install requests, run:

   ```
   pip install requests
   ```

**NOTE**: If you'd like to learn more about requests, see [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/).

## Install and configure `Flask`

Next we need to install Flask. Flask handles the routing for our web app, and allows us to make server-to-server calls that hide our subscription keys from the end user.

1. To install Flask, run:
   ```
   pip install Flask
   ```
   Let's make sure Flask was installed. Run:
   ```
   flask --version
   ```
   The version should be printed to terminal. Anything else means something went wrong.

2. To run the Flask app, you can either use the flask command or Python’s -m switch with Flask. Before you can do that you need to tell your terminal which app to work with by exporting the `FLASK_APP` environment variable:

   **macOS/Linux**:
   ```
   export FLASK_APP=app.py
   ```

   **Windows**:
   ```
   set FLASK_APP=app.py
   ```

## Run the sample

Now that you're all set up, follow these instructions to run the sample. If you'd like a detailed walkthrough of the Python, HTML, and Javascript that pulls this app together, see [Tutorial: Build a Flask app with Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/translator/tutorial-flask-translation-and-synthesis).

1. Open `translate.py` and add the path to your detect and translate container endpoints.
2. Run:
   ```
   flask run
   ```
3. Navigate to the URL provided and test your app.
4. Code for sentiment detection has been left in the codebase, however it has not been adapted to run in a containerised environment due to it's limited language support.

## Clean up

When you're done with the sample, don't forget to shut down your containers.

## Next steps

* [Translator Text API reference](https://docs.microsoft.com/azure/cognitive-services/Translator/reference/v3-0-reference)
* [Text Analytics API reference](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c7)

