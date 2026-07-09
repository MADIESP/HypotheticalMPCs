from os import environ



SESSION_CONFIGS = [
     dict(
        name='Baseline',
        app_sequence=['Part1','Part2'],
        num_demo_participants=20,
        Treatment=0,
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

PARTICIPANT_FIELDS = ['gender','received_stimulus', 'stimulus_amount', 'debt_new', 'debt_repay', 'spending', 'prolific_id', 'spending_net', 'debt_repay_net', 'new_debt_net', 'labor_income_net', 'save_invest_net']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
environ['OTREE_ADMIN_PASSWORD'] = 'MPCs'
environ['OTREE_PRODUCTION'] = '1'
environ['OTREE_AUTH_LEVEL'] = 'STUDY'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2390561968578'

ROOMS = [
    dict(
        name='study0',
        display_name='Study 0'
    ),
    dict(
        name='study1',
        display_name='Study 1'
    ),
    dict(
        name='study2',
        display_name='Study 2'
    ),
]
