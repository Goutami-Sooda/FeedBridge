# -*- encoding: utf-8 -*-
"""
Routes for the Food Bank role.
"""

# TODO edit as required

from flask import render_template
from flask_login import login_required, current_user
from apps.food_bank import blueprint
from apps.authentication.util import role_required
from flask import render_template, jsonify
from apps.food_bank.backend import fetch_food_items


@blueprint.route('/food_bank/profile')
@login_required
@role_required('food_bank')
def food_bank_profile():
    """Food Bank-specific profile page."""
    return render_template('food_bank/profile.html', user=current_user)
'''
@blueprint.route('/food_bank/order')
@login_required
@role_required('food_bank')
def food_bank_requests():
    """View and manage food requests."""
    return render_template('food_bank/order.html', user=current_user)
'''
@blueprint.route('/food_bank/order')
@login_required
@role_required('food_bank')
def food_bank_requests():
    """View and manage food requests."""
    try:
        donors = fetch_food_items()
        return render_template('food_bank/order.html', user=current_user, donors=donors)
    except Exception as e:
        return jsonify({'error': str(e)}), 500