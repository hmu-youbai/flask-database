import time
import pandas as pd
import numpy as np
import yaml
import subprocess
import uuid
from datetime import datetime
from flask import request, Blueprint, render_template, current_app, url_for, redirect, Response, stream_with_context,g, session, Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, BooleanField, StringField, IntegerField, RadioField, HiddenField
from wtforms.validators import DataRequired, Length, Optional, URL


about = Blueprint('about', __name__)


@about.route('/about', methods=['GET', 'POST'])
def index():
    return render_template('about/about.html')
