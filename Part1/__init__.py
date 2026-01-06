from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # --- Page 1: Individual information ---
    age = models.FloatField(label="", max=99)

    gender = models.IntegerField(
        label="",
        choices=[[1, "Man"], [2, "Woman"], [3, "Other/prefer not to say"]],
        widget=widgets.RadioSelectHorizontal
    )

    ethnicity = models.IntegerField(
        label="",
        choices=[[1, "White"], [2, "African American/Black"], [3, "Hispanic/Latino"],
                 [4, "Asian/Asian American"], [5, "Mixed race"], [6, "Other"]],
        widget=widgets.RadioSelect
    )

    education = models.IntegerField(
        label="",
        choices=[[1, "8th Grade or lower"], [2, "Some High School"], [3, "High School degree/GED"],
                 [4, "Some College"], [5, "2-year College Degree"], [6, "4-year College Degree"],
                 [7, "Master's Degree"], [8, "Doctoral Degree"], [9, "Professional Degree (JD or MD)"]],
        widget=widgets.RadioSelect
    )

    marital_status = models.IntegerField(
        label="",
        choices=[[1, "Single"], [2, "Married"], [3, "Legally separated or divorced"], [4, "Widowed"]],
        widget=widgets.RadioSelect
    )

    zip_code = models.StringField(label="")

    employment_status = models.IntegerField(
        label="",
        choices=[[1, "Full-time employee"], [2, "Part-time employee"], [3, "Self-employed or small business owner"],
                 [4, "Unemployed and looking for work"], [5, "Temporarily laid off"], [6, "Student"],
                 [7, "Not currently working and not looking for work"], [8, "Retiree"]],
        widget=widgets.RadioSelect
    )

    occupation_employed = models.IntegerField(
        label="",
        choices=[[1, "Management, business, and financial"], [2, "Professional"], [3, "Service"],
                 [4, "Sales and related"], [5, "Office and administrative support"],
                 [6, "Farming, fishing, and forestry"],
                 [7, "Construction and natural resource extraction"], [8, "Installation, maintenance, and repair"],
                 [9, "Production"], [10, "Transportation and material moving"], [11, "Armed Forces"]],
        blank=True,
        widget=widgets.RadioSelect
    )

    job_flexibility_hours = models.IntegerField(
        label="",
        choices=[[1, "Not at all"], [2, "A little"], [3, "Somewhat"], [4, "A lot"], [5, "Completely"]],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    job_flexibility_overtime = models.IntegerField(
        label="",
        choices=[[1, "No"], [2, "Yes, but rarely"], [3, "Yes, sometimes"], [4, "Yes, frequently"]],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    occupation_unemployed = models.IntegerField(
        label=" ",
        choices=[[1, "Management, business, and financial"], [2, "Professional"], [3, "Service"],
                 [4, "Sales and related"], [5, "Office and administrative support"],
                 [6, "Farming, fishing, and forestry"],
                 [7, "Construction and natural resource extraction"], [8, "Installation, maintenance, and repair"],
                 [9, "Production"], [10, "Transportation and material moving"], [11, "Armed Forces"]],
        blank=True,
        widget=widgets.RadioSelect
    )

    patience_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling) "],[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10 (Very willing)"]],
        widget=widgets.RadioSelect,
        blank=True
    )

    risk_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling)"], [1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10 (Very willing)"]],
        widget=widgets.RadioSelect,
        blank=True
    )

    # --- Household info: Page 2 ---
    household_size = models.IntegerField(
        label=(
            ""
        ),
    choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10 or more"]],
        widget=widgets.RadioSelectHorizontal
    )

    household_children = models.IntegerField(
        label=(
            ""
        ),
        choices=[[0, "0"],[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5 or more"]],
        widget=widgets.RadioSelectHorizontal
    )

    residence_owner = models.IntegerField(
        label=(
            ""
        ),
        choices=[[1, "Own"], [2, "Rent"]],
        widget=widgets.RadioSelectHorizontal
    )
    rent_amount = models.IntegerField(
        label=(
            ""
        ),
        choices=[
            [1, "$0–$399"],
            [2, "$400–$499"],
            [3, "$500–$649"],
            [4, "$650–$799"],
            [5, "$800–$949"],
            [6, "$950–$1,099"],
            [7, "$1,100–$1,299"],
            [8, "$1,300–$1,499"],
            [9, "$1,500–$2,499"],
            [10, "$2,500 –$2,999"],
            [11, "$3,000 or more"],
        ],
        blank=True
    )

    home_value = models.IntegerField(
        label=(
            ""
        ),
        choices=[
            [1, "$0–$49,999"],
            [2, "$50,000–$99,999"],
            [3, "$100,000–$149,999"],
            [4, "$150,000–$199,999"],
            [5, "$200,000–$249,999"],
            [6, "$250,000–$299,999"],
            [7, "$300,000–$349,999"],
            [8, "$350,000–$449,999"],
            [9, "$450,000–$649,999"],
            [10, "$650,000 or more"],
        ],
        blank = True
    )
    household_income_bracket = models.IntegerField(
        label="",

        choices=[[1, "$0–$9,999"], [2, "$10,000–$14,999"], [3, "$15,000–$19,999"],
                 [4, "$20,000–$29,999"], [5, "$30,000–$39,999"], [6, "$40,000–$49,999"],
                 [7, "$50,000–$69,999"], [8, "$70,000–$79,999"], [9, "$80,000–$99,999"],
                 [10, "$100,000–$109,999"], [11, "$110,000–$124,999"], [12, "$125,000–$199,999"],
                 [13, "$200,000 or more"]],
        blank=True
    )

    household_income_exact = models.FloatField(blank=True,
                                               label="")



    # --- Page 3: Household financial questions ---

    financial_decision_making = models.IntegerField(
        label="",
        choices=[
            [1, "I make all the decisions"],
            [2, "I make most of the decisions"],
            [3, "Decisions are shared equally between me and someone else"],
            [4, "Someone else makes most of the decisions"],
            [5, "Someone else makes all the decisions"],
        ],
        widget=widgets.RadioSelect
    )

    financial_awareness = models.IntegerField(
        label=" ",
        choices=[[1, "Not at all informed"], [2, "Somewhat informed"], [3, "Very informed"],
                 [4, "Extremely informed"]],
        widget=widgets.RadioSelect
    )

    grocery_shopping = models.IntegerField(
        label="",
        choices=[[1, "I did the shopping alone "], [2, "I did the shopping with someone else"], [3, "Someone else did the shopping without me"]],
        widget=widgets.RadioSelect
    )

    major_purchase = models.IntegerField(
        label="",
        choices=[[1, "I made the purchase alone"], [2, "I made the purchase with someone else"], [3, "Someone else made the purchase without me"]],
        widget=widgets.RadioSelect
    )


    has_cash = models.BooleanField(label="<b>Cash/checking accounts</b>")
    has_savings = models.BooleanField(label="<b>Savings accounts</b>")
    has_money_market = models.BooleanField(label="<b>Money market/CDs</b>")
    has_stocks = models.BooleanField(label="<b>Stocks, bonds, or mutual funds</b>")
    has_retirement = models.BooleanField(label="<b>Retirement accounts</b><br>"
        "<span style='font-size:0.9em;'>(e.g., 401(k), IRA)</span>")
    has_life_insurance = models.BooleanField(label="<b>Life insurance </b>")
    has_real_estate = models.BooleanField(label="<b>Real estate</b><br>"
        "<span style='font-size:0.9em;'>(other than primary residence)</span>")
    #has_real_estate = models.BooleanField(label="<b>Real estate</b><br>")
    has_other_assets = models.BooleanField(label="<b>Other</b>")

    debt_credit_card = models.BooleanField(label="<b>Credit card debt</b>")
    debt_mortgage = models.BooleanField(label="<b>Mortgage/home equity loans</b>")
    debt_auto = models.BooleanField(label="<b>Auto loans</b>")
    debt_student = models.BooleanField(label="<b>Student loans</b>")
    debt_personal = models.BooleanField(label="<b>Personal/other loans</b>")
    debt_unpaid_bills = models.BooleanField(label="<b>Unpaid bills</b><br>"
        "<span style='font-size:0.9em;'>(utilities, medical, legal, etc.)</span>")

    fico_score = models.IntegerField(
        label="",
        choices=[[1, "579 or lower"], [2, "580–669"], [3, "670–739"], [4, "740–799"], [5, "800 or higher"]],
        widget=widgets.RadioSelect
    )

    bill_payment_ability = models.IntegerField(
        label="",
        choices=[
            [1, "None - all bills are paid on time"],
            [2, "A few are overdue, all by less than a month"],
            [3, "A few are overdue, including some by more than a month"],
            [4, "Around half are overdue"],
            [5, "Most are overdue"]
        ],
        widget=widgets.RadioSelect
    )

    credit_card_payment = models.IntegerField(
        label="",
        choices=[[1, "Always"], [2, "Most months"], [3, "Some months"], [4, "Almost never"], [5, "Never"]],
        widget=widgets.RadioSelect
    )

    housing_payment = models.IntegerField(
        label="",
        choices=[[1, "Always"], [2, "Most months"], [3, "Some months"], [4, "Almost never"], [5, "Never"]],
        widget=widgets.RadioSelect
    )


    # --- Attention Check 1 ---
    attention1 = models.IntegerField(
        label="",
        choices=[[1, "Strongly disagree"], [2, "Disagree"], [3, "Neither agree nor disagree"] ,[4, "Agree"], [5, "Strongly agree"]],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
def gender(player):
    player.participant.gender = player.gender

# PAGES
class Instructions(Page):
    form_model = 'player'

class InstructionsPart1(Page):
    form_model = 'player'


class Page1(Page):
    form_model = 'player'
    form_fields = ['age','gender','ethnicity','education','marital_status','zip_code','employment_status', 'occupation_employed','occupation_unemployed',
                'job_flexibility_hours','job_flexibility_overtime','patience_scale','risk_scale' ]

    def before_next_page(player, timeout_happened):
        gender(player)

    def error_message(self, values):
        if values['risk_scale'] is None:
            return "Please select a value before continuing."
        if values['patience_scale'] is None:
            return "Please select a value before continuing."

class Page2(Page):
    form_model = 'player'
    form_fields = ['household_size','household_children', 'residence_owner', 'rent_amount', 'home_value', 'household_income_bracket','household_income_exact'  ]

    def error_message(self, values):
        if values['residence_owner'] == 2 and values['rent_amount'] is None:
            return "Please provide your monthly rent."

        if values['residence_owner'] == 1 and values['home_value'] is None:
            return "Please provide the value of your home."

        if values['household_income_bracket'] is None:
            return "Please select your household income bracket."




class Page3(Page):
    form_model = 'player'
    form_fields = [
        'financial_decision_making',
        'financial_awareness',
        'grocery_shopping',
        'major_purchase',


        # ---- New ASSET BooleanFields ----
        'has_cash',
        'has_savings',
        'has_money_market',
        'has_stocks',
        'has_retirement',
        'has_life_insurance',
        'has_real_estate',
        'has_other_assets',

        # ---- New DEBT BooleanFields ----
        'debt_credit_card',
        'debt_mortgage',
        'debt_auto',
        'debt_student',
        'debt_personal',
        'debt_unpaid_bills',

        # ---- Remaining fields ----
        'fico_score',
        'bill_payment_ability',
        'credit_card_payment',
        'housing_payment',
        'attention1'
    ]





page_sequence = [Instructions,InstructionsPart1, Page1, Page2,Page3]
#page_sequence = [ Part1]
