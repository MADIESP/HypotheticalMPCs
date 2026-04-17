from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):


    consent = models.BooleanField(
        label="<b>I agree </b> to participate in this study.",
        blank=False,
        widget = widgets.CheckboxInput
    )


    prolific_id = models.StringField(
        label=""
        ,
        blank=False
    )

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
        label=" ",
        choices=[
            [1, "Management, professional, and technical"],
            [2, "Service"],
            [3, "Sales and administrative"],
            [4, "Manual and skilled trades"],
            [5, "Transportation and logistics"],
            [6, "Other occupations"]
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    job_flexibility_hours = models.IntegerField(
        label="",
        choices=[
            [1, "Never"],
            [2, "Rarely"],
            [3, "Sometimes"],
            [4, "Frequently"]
        ],
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
        choices=[
            [1, "Management, professional, and technical"],
            [2, "Service"],
            [3, "Sales and administrative"],
            [4, "Manual and skilled trades"],
            [5, "Transportation and logistics"],
            [6, "Other occupations"]
        ],
        blank=True,
        widget=widgets.RadioSelect
    )

    patience_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling) "],[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6 (Very willing)"]],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

    risk_scale = models.IntegerField(
        label="",
        choices=[[0, "0 (Completely unwilling)"], [1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6 (Very willing)"]],
        widget=widgets.RadioSelectHorizontal,
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

        choices=[[1, "Less than 15.000"], [2, "Between 15.000 and 25.000"], [3, "Between 25.000 and 50.000"],
                 [4, "Between 50.000 and 75.000"], [5, "Between 75.000 and 100.000"], [6, "Between 100.000 and 150.000"],
                 [7, "Between 150.000 and 200.000"], [8, "More than 200.000"]],
        blank=True
    )

    household_income_exact = models.FloatField(blank=True,
                                               label="")

    # covid stimulus

    received_stimulus = models.IntegerField(
        label="",
        choices=[
            [1, "Yes"],
            [2, "No"]
        ],
        widget=widgets.RadioSelect
    )

    stimulus_amount = models.IntegerField(
        label="",
        blank=True
    )



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

    #financial_awareness = models.IntegerField(
        #label=" ",
       # choices=[[1, "Not at all informed"], [2, "Somewhat informed"], [3, "Very informed"],
                 #[4, "Extremely informed"]],
        #widget=widgets.RadioSelect
    #)

   # grocery_shopping = models.IntegerField(
      #  label="",
      #  choices=[[1, "I did the shopping alone "], [2, "I did the shopping with someone else"], [3, "Someone else did the shopping without me"]],
      #  widget=widgets.RadioSelect
   # )

   # major_purchase = models.IntegerField(
      #  label="",
      #  choices=[[1, "I made the purchase alone"], [2, "I made the purchase with someone else"], [3, "Someone else made the purchase without me"]],
       # widget=widgets.RadioSelect
  #  )


    fico_score = models.IntegerField(
        label="",
        choices=[[1, "579 or lower"], [2, "580–669"], [3, "670–739"], [4, "740–799"], [5, "800 or higher"]],
        widget=widgets.RadioSelect
    )

    bill_payment_ability = models.IntegerField(
        label="",
        choices=[
            [1, "Often"],
            [2, "Sometimes"],
            [3, "Rarely"],
            [4, "Never"],
        ],
        widget=widgets.RadioSelect
    )

    credit_card_payment = models.IntegerField(
        label="",
        choices=[[1, "Not applicable (no credit cards or revolving credit)"], [2, "Often"], [3, "Sometimes"], [4, "Rarely"], [5, "Never"]],
        widget=widgets.RadioSelect
    )

    installment_payment = models.IntegerField(
        label="",
        choices=[[1, "Not applicable (no installment loans)"], [2, "Often"], [3, "Sometimes"], [4, "Rarely"], [5, "Never"]],
        widget=widgets.RadioSelect
    )

    payday_payment = models.IntegerField(
        label="",
        choices=[[1, "Not applicable (no payday or short-term loans)"], [2, "Often"], [3, "Sometimes"], [4, "Rarely"],
                 [5, "Never"]],
        widget=widgets.RadioSelect
    )


    # --- Attention Check 1 ---
    attention1 = models.IntegerField(
        label="",
        choices=[[1, "Strongly disagree"], [2, "Disagree"], [3, "Neither agree nor disagree"] ,[4, "Agree"], [5, "Strongly agree"]],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']

def gender(player):
    player.participant.gender = player.gender

def prolific_id(player):
    player.participant.prolific_id = player.prolific_id

def covid_stimulus(player):

    if player.received_stimulus==2:
        player.participant.received_stimulus=2
        player.participant.stimulus_amount = 0
    elif player.received_stimulus==1:
        player.participant.received_stimulus = 1
        player.participant.stimulus_amount=player.stimulus_amount


# PAGES

class Instructions(Page):
    form_model = 'player'
    form_fields = ['prolific_id','consent']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment <3

    def before_next_page(player, timeout_happened):
        prolific_id(player)


class InstructionsT2(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3

    def before_next_page(player, timeout_happened):
        prolific_id(player)

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
    form_fields = ['household_size','household_children', 'residence_owner', 'rent_amount', 'home_value', 'household_income_bracket','household_income_exact', 'received_stimulus','stimulus_amount'  ]

    def error_message(self, values):
        if values['residence_owner'] == 2 and values['rent_amount'] is None:
            return "Please provide your monthly rent."

        if values['residence_owner'] == 1 and values['home_value'] is None:
            return "Please provide the value of your home."

        if values['household_income_bracket'] is None:
            return "Please select your household income bracket."


    def before_next_page(player, timeout_happened):
        covid_stimulus(player)




class Page3(Page):
    form_model = 'player'
    form_fields = [
        'financial_decision_making',


        # ---- Remaining fields ----
        'fico_score',
        'bill_payment_ability',
        'credit_card_payment',
        'installment_payment',
        'payday_payment',
        'attention1'
    ]





page_sequence = [Instructions, InstructionsT2,  Page1, Page2,Page3]
#page_sequence = [ Page1, Page2]
