from flask import jsonify
from flask.views import MethodView
from webargs import fields, validate
from webargs.flaskparser import use_args, parser, abort
from textstat import textstat

class Readability(MethodView):
    text_args = {"text": fields.Str(required=True)}

    def get(self):
        return "Post your text to this resource to retrieve the readability."

    @use_args(text_args)
    def post(self, args):
        text = args['text']
        readability = {}
        readability["flesch_reading_ease"] = textstat.flesch_reading_ease(text)
        readability["flesch_kincaid_grade"] = textstat.flesch_kincaid_grade(text)
        readability["smog_index"] = textstat.smog_index(text)
        readability["coleman_liau_index"] = textstat.coleman_liau_index(text)
        readability["automated_readability_index"] = textstat.automated_readability_index(text)
        readability["dale_chall_readability_score"] = textstat.dale_chall_readability_score(text)
        readability["linsear_write_formula"] = textstat.linsear_write_formula(text)
        readability["gunning_fog"] = textstat.gunning_fog(text)
        readability["text_standard"] = textstat.text_standard(text)
        readability["difficult_words"] = textstat.difficult_words(text)
        return jsonify(readability)