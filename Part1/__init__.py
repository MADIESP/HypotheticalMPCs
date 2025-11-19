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
    # --- Demographics ---
    age = models.FloatField(label=" <b> 1. What is your age? </b>", max=99)

    gender = models.IntegerField(
        label="<b> 2. What is your gender? </b>",
        choices=[[1, "Man"], [2, "Woman"], [3, "Other"]],
        widget=widgets.RadioSelectHorizontal
    )

    ethnicity = models.IntegerField(
        label="<b> 3. How would you describe your ethnicity/race?</b>",
        choices=[[1, "White"], [2, "African American/Black"], [3, "Hispanic/Latino"],
                 [4, "Asian/Asian American"], [5, "Mixed race"], [6, "Other"]],
        widget=widgets.RadioSelect
    )

    education = models.IntegerField(
        label="<b> 4. What is your highest level of education?</b>",
        choices=[[1, "Eighth Grade or lower"], [2, "Some High School"], [3, "High School degree/GED"],
                 [4, "Some College"], [5, "2-year College Degree"], [6, "4-year College Degree"],
                 [7, "Master's Degree"], [8, "Doctoral Degree"], [9, "Professional Degree (JD or MD)"]],
        widget=widgets.RadioSelect
    )

    marital_status = models.IntegerField(
        label="<b> 5. What is your marital status?</b>",
        choices=[[1, "Single"], [2, "Married"], [3, "Legally separated or divorced"], [4, "Widowed"]],
        widget=widgets.RadioSelect
    )

    zip_code = models.StringField(label="<b>What is your current ZIP code?</b>")

    # --- Household info ---
    household_size = models.IntegerField(
        label="<b> 6. How many people, including yourself, currently live in your household? <br> <i> By 'household' we mean everyone who usually lives with you in your primary residence including yourself (but excluding roommates and renters). </i></b>",
        choices=[[1, "1"], [2, "2"], [3, "3"], [4, "4"], [5, "5"],
                 [6, "6"], [7, "7"], [8, "8"], [9, "9"], [10, "10 or more"]],
        widget=widgets.RadioSelectHorizontal
    )


    # --- Employment ---
    employment_status = models.IntegerField(
        label="<b> 7. What is your current employment status?</b>",
        choices=[[1, "Full-time employee"], [2, "Part-time employee"], [3, "Self-employed or small business owner"],
                 [4, "Unemployed and looking for work"], [5, "Temporarily laid off"], [6, "Student"],
                 [7, "Not currently working and not looking for work"], [8, "Retiree"]],
        widget=widgets.RadioSelect
    )

    occupation_employed = models.IntegerField(
        label="<b> 8. Which category best describes your main occupation?</b>",
        choices=[[1, "Management, business, and financial"], [2, "Professional"], [3, "Service"],
                 [4, "Sales and related"], [5, "Office and administrative support"],
                 [6, "Farming, fishing, and forestry"],
                 [7, "Construction and natural resource extraction"], [8, "Installation, maintenance, and repair"],
                 [9, "Production"], [10, "Transportation and material moving"], [11, "Armed Forces"]],
        blank=True,
        widget=widgets.RadioSelect
    )

    job_flexibility_hours = models.IntegerField(
        label="<b> 9. To what extent can you choose or change your work hours (start and end times, number of hours)?</b>",
        choices=[[1, "Not at all"], [2, "A little"], [3, "Somewhat"], [4, "A lot"], [5, "Completely"]],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    job_flexibility_overtime = models.IntegerField(
        label="<b> 10. Is it possible for you to take extra shifts, accept overtime, or pick up additional hours on short notice?</b>",
        choices=[[1, "No"], [2, "Yes, but rarely"], [3, "Yes, sometimes"], [4, "Yes, frequently"]],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )

    occupation_unemployed = models.IntegerField(
        label="<b> 8. Which category best describes your most recent main occupation?</b>",
        choices=[[1, "Management, business, and financial"], [2, "Professional"], [3, "Service"],
                 [4, "Sales and related"], [5, "Office and administrative support"],
                 [6, "Farming, fishing, and forestry"],
                 [7, "Construction and natural resource extraction"], [8, "Installation, maintenance, and repair"],
                 [9, "Production"], [10, "Transportation and material moving"], [11, "Armed Forces"]],
        blank=True,
        widget=widgets.RadioSelect
    )

    # --- Household financial questions ---
    financial_decision_making = models.IntegerField(
        label="<b> 1. Which of the following best describes how financial decisions are made in your household?</b>",
        choices=[[1, "Someone else makes all"], [2, "Someone else makes most"], [3, "Shared equally"],
                 [4, "I make most"], [5, "I make all"]],
        widget=widgets.RadioSelectHorizontal
    )

    financial_awareness = models.IntegerField(
        label="<b> 2. Think about how precisely you would be able to list all your sources of income and all your expenses. (Don't worry, we will not ask you about this in more detail!)</b> <br> <br> <b>	How informed are you about where the money in your household is coming from and what exactly it is being spend on? </b> ",
        choices=[[1, "Not at all informed"], [2, "Somewhat informed"], [3, "Very informed"],
                 [4, "Extremely informed"]],
        widget=widgets.RadioSelectHorizontal
    )

    grocery_shopping = models.IntegerField(
        label="<b> 3. Who did the last grocery shopping for your household?</b>",
        choices=[[1, "I did"], [2, "Another household member"], [3, "We decided together"]],
        widget=widgets.RadioSelectHorizontal
    )

    major_purchase = models.IntegerField(
        label="<b> 4. Who made the last purchase of a big item (costing more than $1000) for your household?</b>",
        choices=[[1, "I did"], [2, "Another household member"], [3, "We decided together"]],
        widget=widgets.RadioSelectHorizontal
    )

    household_income_bracket = models.IntegerField(
        label="<b> 5. What was your total household income, before taxes and transfers, in 2024? </b> <br> <i> <b>  Note that social insurance benefits (e.g., Social Security, Medicare, unemployment insurance) are included in this definition of income. </b> </i>",

        choices=[[1, "$0–$9,999"], [2, "$10,000–$14,999"], [3, "$15,000–$19,999"],
                 [4, "$20,000–$29,999"], [5, "$30,000–$39,999"], [6, "$40,000–$49,999"],
                 [7, "$50,000–$69,999"], [8, "$70,000–$79,999"], [9, "$80,000–$99,999"],
                 [10, "$100,000–$109,999"], [11, "$110,000–$124,999"], [12, "$125,000–$199,999"],
                 [13, "$200,000 or more"]],
        widget=widgets.RadioSelectHorizontal
    )

    household_income_exact = models.FloatField(blank=True,
                                               label="<b> More precisely, how much would you say it is? </b>")

    has_cash = models.BooleanField(label="<b>Cash/checking accounts</b>")
    has_savings = models.BooleanField(label="<b>Savings accounts</b>")
    has_money_market = models.BooleanField(label="<b>Money market/CDs</b>")
    has_stocks = models.BooleanField(label="<b>Stocks, bonds, or mutual funds</b>")
    has_retirement = models.BooleanField(label="<b>Retirement accounts (e.g., 401(k), IRA)</b>")
    has_life_insurance = models.BooleanField(label="<b>Life insurance with cash value</b>")
    has_real_estate = models.BooleanField(label="<b>Real estate (other than primary residence)</b>")
    has_other_assets = models.BooleanField(label="<b>Other</b>")

    debt_credit_card = models.BooleanField(label="<b>Credit card debt</b>")
    debt_mortgage = models.BooleanField(label="<b>Mortgage/home equity loans</b>")
    debt_auto = models.BooleanField(label="<b>Auto loans</b>")
    debt_student = models.BooleanField(label="<b>Student loans</b>")
    debt_personal = models.BooleanField(label="<b>Personal/other loans</b>")
    debt_unpaid_bills = models.BooleanField(label="<b>Unpaid bills (utilities, medical, legal, etc.)</b>")

    fico_score = models.IntegerField(
        label="<b> 8. What is the highest FICO credit score in your household?</b>",
        choices=[[1, "579 or lower"], [2, "580–669"], [3, "670–739"], [4, "740–799"], [5, "800 or higher"]],
        widget=widgets.RadioSelectHorizontal
    )

    bill_payment_ability = models.IntegerField(
        label="<b>9. How many of your household's bills are usually overdue?</b>",
        choices=[
            [1, "None - all bills are paid on time"],
            [2, "A few are overdue, but by less than a month"],
            [3, "Around half are overdue"],
            [4, "Most are overdue"]
        ],
        widget=widgets.RadioSelectHorizontal
    )

    credit_card_payment = models.IntegerField(
        label="<b> 10. How often are you able to pay your household credit card balances in full?</b>",
        choices=[[1, "Always"], [2, "Most months"], [3, "Some months"], [4, "Almost never"], [5, "Never"]],
        widget=widgets.RadioSelectHorizontal
    )

    housing_payment = models.IntegerField(
        label="<b> 11. How often are you able to make your household full rent, mortgage, or loan payments on time? </b>",
        choices=[[1, "Always"], [2, "Most months"], [3, "Some months"], [4, "Almost never"], [5, "Never"]],
        widget=widgets.RadioSelectHorizontal
    )

    # --- 13. Time preference ---
    patience_scale = models.StringField(
        label="<b> 12. In general, how willing are you to give up something beneficial today in order to benefit more in the future?</b>",
        choices=["0 (Completely unwilling)", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 (Very willing)"],
        widget=widgets.RadioSelectHorizontal,
    )

    # --- 14. Risk preference ---
    risk_scale = models.StringField(
        label="<b> 13. In general, how willing are you to take risks?</b>",
        choices=["0 (Completely unwilling)", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10 (Very willing)"],
        widget=widgets.RadioSelectHorizontal,
    )

# FUNCTIONS
def gender(player):
    player.participant.gender = player.gender

# PAGES
class Instructions(Page):
    form_model = 'player'


class Part1(Page):
    form_model = 'player'
    form_fields = ['age','gender','ethnicity','education','marital_status','zip_code']

    def before_next_page(player, timeout_happened):
        gender(player)

class Part2(Page):
    form_model = 'player'
    form_fields = ['household_size','employment_status']



class Part3(Page):
    form_model = 'player'

    def get_form_fields(player):
        employed_statuses = [1, 2, 3]

        # If employed → show job-related questions
        if player.employment_status in employed_statuses:
            return [
                'occupation_employed',
                'job_flexibility_hours',
                'job_flexibility_overtime'
            ]
        # If unemployed or other → show most recent occupation
        else:
            return ['occupation_unemployed']

    # Only display Part3 if the player has answered employment_status in Part2
    def is_displayed(player):
        return player.employment_status is not None and player.employment_status != 6



class Part4(Page):
    form_model = 'player'
    form_fields = [
        'financial_decision_making',
        'financial_awareness',
        'grocery_shopping',
        'major_purchase',
        'household_income_bracket',
        'household_income_exact',

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
        'patience_scale',
        'risk_scale'
    ]

page_sequence = [Instructions, Part1, Part2,Part3,Part4]
#page_sequence = [ Part1]
