django-floppyforms-bootstrap3
=============================

Bootstrap 3 Friendly Templates for Django Floppy Forms

The aim of this is to provide Django Floppy Forms templates that produce nice Bootstrap 3 HTML with
minimal effort, so you can get something nice looking for your Bootstrap powered site quickly and
easily, and also to give a starting point for further customisation.

This project is currently incomplete. I'm only implementing bits as and when I need them. However,
I am very happy to receive merge requests that get more of it finished.

What Works So Far?
==================

* The Bootstrap 3 Horizontal Form layout http://getbootstrap.com/css/#forms-horizontal

How To Use
==========

* Clone the git repo into the base directory of your Django Project, and add it to settings.py just like any other app.
* Make sure this app is included in setings.py apps *before* floppy forms, as otherwise the template overriding doesn't seem to work properly.
* Use floppyforms as normal.
* Start with the example code below for how to use it.

Example
=======

The example below gives a Bootstrap 3 Horizontal Form Layout.

    <div class="row">
      <form class="form-horizontal" role="form" action="{% url 'comment' %}" method="post">
        {% csrf_token %}
        {% form comment_form using "floppyforms/layouts/bootstrap3-horizontal.html" %}
        <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">
            <button type="submit" class="btn btn-default">Post Comment</button>
          </div>
        </div>
      </form>
    </div>

Sources
=======

The code in this repository was based off the Bootstrap 2 example in the FloppyForms documentation,
as well as comments at https://github.com/gregmuellegger/django-floppyforms/issues/86


