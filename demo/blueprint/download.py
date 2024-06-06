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


download = Blueprint('download', __name__)


@download.route('/download', methods=['GET', 'POST'])
def index():
    csv_path = 'Download_dataset.csv'
    data = pd.read_csv(csv_path).to_dict(orient='records')
    return render_template('download/download.html',  data=data)
