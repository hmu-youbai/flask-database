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
from flask_sqlalchemy import SQLAlchemy

search = Blueprint('search', __name__)
db = SQLAlchemy()
class Gene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80), unique=True, nullable=False)
    ensembl = db.Column(db.String(120), unique=True, nullable=False)


@search.route('/search', methods=['GET', 'POST'])
def index():
    return render_template('search/search.html')





@search.route('/fetch-data', methods=['POST'])
def fetch_data():
    id_type = request.form.get('idType')
    id_value = request.form.get('idValue')
    if id_type=="ensembl":
        gene = Gene.query.filter_by(ensembl=id_value).first()
        id_value=gene.symbol
    about_path='demo/static/images/'+ id_value +'_about.txt'
    about_list=[]
    with open(about_path) as file:
        for line in file:
            about_list.append(line.strip())
    if len(about_list)==6:
        name=id_value
        full_name=about_list[1]
        aliases=about_list[2]
        location=about_list[3]
        description=about_list[4]
        genecards=f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={id_value}"
        ncbi=f"https://www.ncbi.nlm.nih.gov/gene/?term={id_value}"
        ensembl=f"https://asia.ensembl.org/Homo_sapiens/Search/Results?q={id_value};site=ensembl;facet_species=Human"
        wikigenes=f"https://www.wikigenes.org/?search={id_value}&db=_any&cat=&type=&field=&org=&action=go&ftype=0"
    else:
        name=id_value
        full_name=""
        aliases=""
        location=""
        description=""
        genecards=f"https://www.genecards.org/cgi-bin/carddisp.pl?gene={id_value}"
        ncbi=f"https://www.ncbi.nlm.nih.gov/gene/?term={id_value}"
        ensembl=f"https://asia.ensembl.org/Homo_sapiens/Search/Results?q={id_value};site=ensembl;facet_species=Human"
        wikigenes=f"https://www.wikigenes.org/?search={id_value}&db=_any&cat=&type=&field=&org=&action=go&ftype=0"
        
        
    featurePlot = url_for('static', filename='images/'+ id_value +'_featureplot_umap.png')
    featurePlot2 = url_for('static', filename='images/'+ id_value +'_featureplot_tsne.png')
    violinPlot = url_for('static', filename='images/'+ id_value +'_violin.png')
    developmentalStages = url_for('static', filename='images/'+ id_value +'_stage.png')
    cellTypeResult = url_for('static', filename='images/'+ id_value +'_type.png')
    response_data = {
        'featurePlot': featurePlot,
        'featurePlot2': featurePlot2,
        'violinPlot': violinPlot,
        'developmentalStages': developmentalStages,
        'cellTypeResult': cellTypeResult,
        'genename':name,
        'full_name':full_name,
        'aliases':aliases,
        'location':location,
        'description':description,
        'genecards':genecards,
        'ncbi':ncbi,
        'ensembl':ensembl,
        'wikigenes':wikigenes,
    }
    return jsonify(response_data)











@search.route('/suggest-genes', methods=['GET'])
def suggest_genes():
    query_type = request.args.get('query_type', '').lower()
    query = request.args.get('query', '').lower()
    if query_type == "symbol":
        matching_genes = Gene.query.filter(Gene.symbol.like(f"%{query}%")).limit(8).all()
        suggestions = [gene.symbol for gene in matching_genes]
        return jsonify(suggestions)
    else:
        matching_genes = Gene.query.filter(Gene.ensembl.like(f"%{query}%")).limit(8).all()
        suggestions = [gene.ensembl for gene in matching_genes]
        return jsonify(suggestions)




