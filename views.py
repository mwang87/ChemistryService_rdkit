# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for, send_file, make_response

from app import app

import os
import csv
import json
import uuid
import requests
from rdkit import Chem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols

@app.route("/structure_similarity/smiles")
def smilessimilarity():
    structure_1 = request.args.get('structure1')
    structure_2 = request.args.get('structure2')

    m1 = Chem.MolFromSmiles(structure_1)
    m2 = Chem.MolFromSmiles(structure_2)

    fp1 = FingerprintMols.FingerprintMol(m1)
    fp2 = FingerprintMols.FingerprintMol(m2)

    similarity_tanimoto = DataStructs.FingerprintSimilarity(fp1,fp2)

    return_dict = {}
    return_dict["similarity"] = similarity_tanimoto

    return json.dumps(return_dict)

@app.route('/heartbeat', methods=['GET'])
def testapi():
    return_obj = {}
    return_obj["status"] = "success"
    return json.dumps(return_obj)
