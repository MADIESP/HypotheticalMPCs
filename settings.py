from os import environ



SESSION_CONFIGS = [
     dict(
        name='Baseline',
        app_sequence=['Part1','Part2'],
        num_demo_participants=20,
        Treatment=1,
        completionlink= 'https://app.prolific.com/submissions/complete?cc=CY9R67RM',

     ),
    dict(
        name='T1',
        app_sequence=['Part1','Part2'],
        num_demo_participants=20,
        Treatment=2,
        completionlink= 'https://app.prolific.com/submissions/complete?cc=CY9R67RM',
    ),
    dict(
        name='T2',
        app_sequence=['Part1', 'Part2'],
        num_demo_participants=20,
        Treatment=3,
        completionlink= 'https://app.prolific.com/submissions/complete?cc=CY9R67RM',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['gender','received_stimulus', 'stimulus_amount', 'debt_new', 'debt_repay', 'payoff_questions', 'prolific_id']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
#ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2390561968578'

environ['OTREE_ADMIN_PASSWORD'] = 'HypotheticalMPCs'
environ['OTREE_PRODUCTION'] = '1'
environ['OTREE_AUTH_LEVEL'] ='STUDY'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
AUTH_LEVEL= environ.get('OTREE_AUTH_LEVEL')

ROOMS = [

    dict(
        name='consumption_savings_study1',
        display_name='consumption_savings_study1'
    ),
dict(
        name='consumption_savings_study2',
        display_name='consumption_savings_study2'
    ),
dict(
        name='consumption_savings_study3',
        display_name='consumption_savings_study3'
    ),
]