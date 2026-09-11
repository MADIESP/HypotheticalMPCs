from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Part2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    Treatment = models.IntegerField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
# ================= SPENDING =================

    spend_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    spend_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    spend_amount = models.CurrencyField(min=0, blank=True)

    spend_everyday = models.CurrencyField(min=0, blank=True)
    spend_leisure = models.CurrencyField(min=0, blank=True)
    spend_services = models.CurrencyField(min=0, blank=True)
    spend_durable = models.CurrencyField(min=0, blank=True)

    # ================= PAYMENT METHOD FOR ADDITIONAL SPENDING =================
    spend_pay_credit_card = models.CurrencyField(min=0, blank=True)
    spend_pay_debit_card = models.CurrencyField(min=0, blank=True)
    spend_pay_cash = models.CurrencyField(min=0, blank=True)
    spend_pay_bank_transfer = models.CurrencyField(min=0, blank=True)
    spend_pay_bnpl = models.CurrencyField(min=0, blank=True)
    spend_pay_store_financing = models.CurrencyField(min=0, blank=True)
    spend_pay_bills_later = models.CurrencyField(min=0, blank=True)
    spend_pay_prepaid = models.CurrencyField(min=0, blank=True)
    spend_pay_other = models.CurrencyField(min=0, blank=True)
    spend_cc_repaid = models.CurrencyField(min=0, blank=True)
    spend_cc_fraction_paid = models.IntegerField(min=0, max=100, blank=True)
    spend_cc_remaining_timing = models.StringField(
        choices=[
            ('within_one_month', "By the next statement's due date"),
            ('one_to_three_months', 'By a statement due date 2 to 3 months later'),
            ('more_than_three_months', 'By a statement due date more than 3 months later'),
            ('not_sure', 'I am not sure'),
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )
    spend_cc_timing_specify = models.LongStringField(blank=True)

    spend_other_paylater_repaid = models.CurrencyField(min=0, blank=True)
    spend_other_paylater_fraction_paid = models.IntegerField(min=0, max=100, blank=True)
    spend_other_paylater_remaining_timing = models.StringField(
        choices=[
            ('within_one_month', 'Within one month after it is due'),
            ('one_to_three_months', '1 to 3 months after it is due'),
            ('more_than_three_months', 'More than 3 months after it is due'),
            ('not_sure', 'I am not sure'),
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )
    spend_other_paylater_timing_specify = models.LongStringField(blank=True)

    # ================= DEBT REPAYMENT =================
    debt_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    debt_same_or_decrease = models.StringField(
        choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
        widget=widgets.RadioSelect,
        blank=True
    )
    debt_amount = models.CurrencyField(min=0, blank=True)

    debt_cc = models.CurrencyField(min=0, blank=True)
    debt_bills = models.CurrencyField(min=0, blank=True)
    debt_short = models.CurrencyField(min=0, blank=True)
    debt_long = models.CurrencyField(min=0, blank=True)

    debt_repay_description = models.LongStringField(blank=True)
    spending_description = models.LongStringField(blank=True)

    # ================= LABOR =================
    labor_decrease = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect
    )
    labor_same_or_increase = models.StringField(
        choices=[('same', 'Keep the same'), ('increase', 'Increase')],
        widget=widgets.RadioSelect,
        blank=True
    )
    labor_hours = models.FloatField(min=0, blank=True)
    labor_income = models.CurrencyField(min=0, blank=True)

    labor_gigs = models.CurrencyField(min=0, blank=True)
    labor_overtime = models.CurrencyField(min=0, blank=True)
    labor_holidays = models.CurrencyField(min=0, blank=True)
    labor_contract = models.CurrencyField(min=0, blank=True)

    # ================= NEW DEBT =================
    newdebt_same_or_decrease = models.StringField(
    choices=[('same', 'Keep the same'), ('decrease', 'Decrease')],
    widget=widgets.RadioSelect,
        blank=True
    )

    newdebt_increase = models.StringField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=widgets.RadioSelect,
        blank=True
    )
    newdebt_amount = models.CurrencyField(min=0, blank=True)

    newdebt_cc = models.CurrencyField(min=0, blank=True)
    newdebt_bills = models.CurrencyField(min=0, blank=True)
    newdebt_short = models.CurrencyField(min=0, blank=True)
    newdebt_long = models.CurrencyField(min=0, blank=True)

    spending = models.IntegerField(min=-10000, max=10000)
    save_invest = models.IntegerField(min=-10000, max=10000)
    debt_repay = models.IntegerField(min=-10000, max=10000)
    debt_new = models.IntegerField(min=-10000, max=10000)
    labor = models.IntegerField(min=-10000, max=10000)

    # 0–10 integer scales
    understanding_difficulty = models.IntegerField(
        label="",choices=[0,1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal
    )

    mental_effort = models.IntegerField(
        label="",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal
    )

    # Category coverage question
    categories_cover = models.IntegerField(
        label="",
        choices=[
            [0, "Yes, all of my uses fit the categories"],
            [1, "No"],
        ],
        widget=widgets.RadioSelect
    )
    attention2 = models.IntegerField(
        label="",
        choices=[[1, "Not at all concerned"],
                 [2, "Slightly concerned"],[3, "Moderately concerned"],[4, "Very concerned"],[5, "Extremely concerned"]],
        widget=widgets.RadioSelectHorizontal,
    )

    categories_specify = models.LongStringField(
        label="Please specify:",
        blank=True
    )

    #Scenarios

    spending_Robin = models.IntegerField(min=-1500, max=1500)
    save_invest_Robin = models.IntegerField(min=-1500, max=1500)
    debt_repay_Robin = models.IntegerField(min=-1500, max=1500)
    debt_new_Robin = models.IntegerField(min=-1500, max=1500)
    labor_Robin = models.IntegerField(min=-1500, max=1500)
    labor_hours_Robin = models.FloatField(blank=True)
    spending_Charlie = models.IntegerField(min=-1500, max=1500)
    save_invest_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_repay_Charlie = models.IntegerField(min=-1500, max=1500)
    debt_new_Charlie = models.IntegerField(min=-1500, max=1500)
    labor_Charlie = models.IntegerField(min=-1500, max=1500)
    labor_hours_Charlie = models.FloatField(blank=True)
    spending_Morgan = models.IntegerField(min=-1500, max=1500)
    save_invest_Morgan = models.IntegerField(min=-1500, max=1500)
    debt_repay_Morgan = models.IntegerField(min=-1500, max=1500)
    debt_new_Morgan = models.IntegerField(min=-1500, max=1500)
    labor_Morgan = models.IntegerField(min=-1500, max=1500)
    labor_hours_Morgan = models.FloatField(blank=True)
    training_trials_Robin = models.IntegerField(initial=0)
    training_trials_Charlie = models.IntegerField(initial=0)
    training_trials_Morgan = models.IntegerField(initial=0)
    training_first_Robin_spending = models.IntegerField(initial=0)
    training_first_Robin_save_invest = models.IntegerField(initial=0)
    training_first_Robin_debt_repay = models.IntegerField(initial=0)
    training_first_Robin_debt_new = models.IntegerField(initial=0)
    training_first_Robin_labor = models.IntegerField(initial=0)
    training_first_Robin_labor_hours = models.FloatField(initial=0)
    training_first_Charlie_spending = models.IntegerField(initial=0)
    training_first_Charlie_save_invest = models.IntegerField(initial=0)
    training_first_Charlie_debt_repay = models.IntegerField(initial=0)
    training_first_Charlie_debt_new = models.IntegerField(initial=0)
    training_first_Charlie_labor = models.IntegerField(initial=0)
    training_first_Charlie_labor_hours = models.FloatField(initial=0)
    training_first_Morgan_spending = models.IntegerField(initial=0)
    training_first_Morgan_save_invest = models.IntegerField(initial=0)
    training_first_Morgan_debt_repay = models.IntegerField(initial=0)
    training_first_Morgan_debt_new = models.IntegerField(initial=0)
    training_first_Morgan_labor = models.IntegerField(initial=0)
    training_first_Morgan_labor_hours = models.FloatField(initial=0)
    categories_cover_scenario = models.IntegerField(
        label="",
        choices=[
            [0, "Yes, all of their uses fit the categories"],
            [1, "No, some categories were missing or did not fit"],
        ],
        widget=widgets.RadioSelect
    )

    categories_specify_scenario = models.LongStringField(
        label="Please specify:",
        blank=True
    )

    final_comments = models.LongStringField(
        label="Thank you for taking the survey. Do you have any questions or comments for us?",
        blank=True
    )

    payment_intended_for = models.IntegerField(
        label="",
        choices=[[1, "For me personally"],
            [2, "For the entire household (joint money)"],[3,"Not sure"]],
        widget=widgets.RadioSelect,
    )

    payment_access = models.StringField(
        label="",
        choices=[
            [1,"Only me"],
            [2,"Me and other household members"],
            [3,"Not sure"]],
        widget=widgets.RadioSelect,
    )

    payment_different_if_personal = models.StringField(
        label="",
        choices=[
            "Yes",
            "No",
            "Not sure",
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    payment_different_explain = models.LongStringField(
        label="<b> How would your answers have changed? Please explain: </b>",
        blank=True,
    )

    deposit_account = models.IntegerField(
        label="",
        choices=[
            [1, "On an account to which only I have access"],
            [2, "On a joint account shared with other household members"],
            [3, "On an account to which I do not have access"],
            [4, "Not sure"],
        ],
        widget=widgets.RadioSelect
    )


# FUNCTIONS

def creating_session(subsession: Subsession):
    subsession.Treatment = subsession.session.config['Treatment']

def is_baseline(player):
    return player.subsession.Treatment in [0, 1, 5]


def participant_value(player, field_name, default=None):
    return getattr(player.participant, field_name, default)


def is_t5_covid_received(player):
    return player.subsession.Treatment == 6 and participant_value(player, 'received_stimulus') == 1


def is_t5_hypothetical(player):
    return player.subsession.Treatment == 6 and participant_value(player, 'received_stimulus') != 1


def uses_two_category_elicitation(player):
    return is_baseline(player) or player.subsession.Treatment == 6


def uses_open_descriptions(player):
    return player.subsession.Treatment in [5, 6]


def actual_stimulus_elicitation(player):
    return (
        player.subsession.Treatment == 3
        and participant_value(player, 'received_stimulus') == 1
    ) or is_t5_covid_received(player)


def actual_payment_label(player):
    if player.subsession.Treatment == 6:
        return 'unexpected one-time payment'
    return 'Covid stimulus payment'


def actual_payment_label_with_amount(player):
    amount = int(participant_value(player, 'stimulus_amount', 0) or 0)
    return f'${amount} {actual_payment_label(player)}'


def has_training_examples(player):
    return False


def is_t4_training(player):
    return has_training_examples(player)


def scenario_pronouns(player):
    gender = player.participant.gender
    if gender == 1:
        return dict(pronoun_subject="he", pronoun_object="his")
    if gender == 2:
        return dict(pronoun_subject="she", pronoun_object="her")
    return dict(pronoun_subject="they", pronoun_object="their")


def validate_training_response(values, expected, hints):
    for field, target in expected.items():
        value = values.get(field)
        if value is None:
            value = 0
        if isinstance(target, float):
            if abs(float(value or 0) - target) > 0.01:
                return hints[field]
        elif int(value or 0) != target:
            return hints[field]
    return None


def add_training_trial(player, field_name):
    current = player.field_maybe_none(field_name) or 0
    setattr(player, field_name, current + 1)


def save_first_training_attempt(player, scenario_name, values):
    trial_field = f'training_trials_{scenario_name}'
    if player.field_maybe_none(trial_field):
        return

    for category in ['spending', 'save_invest', 'debt_repay', 'debt_new', 'labor', 'labor_hours']:
        source_field = f'{category}_{scenario_name}'
        target_field = f'training_first_{scenario_name}_{category}'
        setattr(player, target_field, values.get(source_field) or 0)


def debtBaseline(player):
    if player.debt_increase == 'yes':
        debt_repay = int(player.debt_amount or 0)
    elif player.debt_same_or_decrease == 'decrease':
        debt_repay = -int(player.debt_amount or 0)
    else:
        debt_repay = 0

    if player.spend_increase == 'yes':
        spending = int(player.spend_amount or 0)
    elif player.spend_same_or_decrease == 'decrease':
        spending = -int(player.spend_amount or 0)
    else:
        spending = 0

    player.debt_repay = debt_repay
    player.spending = spending
    player.participant.debt_repay = debt_repay
    player.participant.spending = spending
    player.participant.debt_repay_net = debt_repay
    player.participant.spending_net = spending

def save_elicitation_totals(player):
    def signed(first, second, amount, yes_sign=1):
        if first == 'yes':
            return int(amount or 0) * yes_sign
        if second in ['decrease', 'increase']:
            sign = -1 if second == 'decrease' else 1
            return int(amount or 0) * sign
        return 0

    spending = signed(
        player.field_maybe_none('spend_increase'),
        player.field_maybe_none('spend_same_or_decrease'),
        player.field_maybe_none('spend_amount'),
    )
    debt_repay = signed(
        player.field_maybe_none('debt_increase'),
        player.field_maybe_none('debt_same_or_decrease'),
        player.field_maybe_none('debt_amount'),
    )
    debt_new = signed(
        player.field_maybe_none('newdebt_increase'),
        player.field_maybe_none('newdebt_same_or_decrease'),
        player.field_maybe_none('newdebt_amount'),
    )
    labor = signed(
        player.field_maybe_none('labor_decrease'),
        player.field_maybe_none('labor_same_or_increase'),
        player.field_maybe_none('labor_income'),
        yes_sign=-1,
    )
    base_amount = 1000
    if actual_stimulus_elicitation(player):
        base_amount = int(participant_value(player, 'stimulus_amount', 0) or 0)
    save_invest = base_amount - spending - debt_repay + debt_new + labor

    player.spending = spending
    player.debt_repay = debt_repay
    player.debt_new = debt_new
    player.labor = labor
    player.save_invest = save_invest

    player.participant.spending = spending
    player.participant.debt_repay = debt_repay
    player.participant.debt_new = debt_new
    player.participant.spending_net = spending
    player.participant.debt_repay_net = debt_repay
    player.participant.new_debt_net = debt_new
    player.participant.labor_income_net = labor
    player.participant.save_invest_net = save_invest

    # PAGES

class InstructionsPart2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return (
            is_baseline(player)
            or player.subsession.Treatment == 2
            or player.subsession.Treatment == 4
            or player.subsession.Treatment == 3 and participant_value(player, 'received_stimulus') == 2
            or is_t5_hypothetical(player)
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t4=has_training_examples(player))


class InstructionsPart2T2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return actual_stimulus_elicitation(player)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            payment_label_with_amount=actual_payment_label_with_amount(player),
        )


class instructionsT0(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return uses_two_category_elicitation(player)

    @staticmethod
    def vars_for_template(player: Player):
        payment_amount = 1000
        if is_t5_covid_received(player):
            payment_amount = int(participant_value(player, 'stimulus_amount', 0) or 0)
        return dict(
            is_covid_actual=is_t5_covid_received(player),
            payment_label=actual_payment_label(player),
            payment_label_with_amount=actual_payment_label_with_amount(player),
            payment_amount=payment_amount,
        )


class instructionsT1(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.subsession.Treatment == 2
            or player.subsession.Treatment == 4
            or player.subsession.Treatment == 3 and participant_value(player, 'received_stimulus') == 2
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t4=has_training_examples(player))

class instructionsT2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 3 and participant_value(player, 'received_stimulus') == 1


class ElicitationT0(Page):
    form_model = 'player'
    form_fields = [
        'debt_increase', 'debt_same_or_decrease', 'debt_amount',
        'debt_cc', 'debt_bills', 'debt_short', 'debt_long',
        'debt_repay_description',
        'spend_increase', 'spend_same_or_decrease', 'spend_amount',
        'spend_everyday', 'spend_leisure', 'spend_services', 'spend_durable',
        'spending_description',
        'spending', 'debt_repay',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return uses_two_category_elicitation(player)

    @staticmethod
    def vars_for_template(player: Player):
        payment_amount = 1000
        if is_t5_covid_received(player):
            payment_amount = int(participant_value(player, 'stimulus_amount', 0) or 0)
        return dict(
            is_t4=uses_open_descriptions(player),
            is_covid_actual=is_t5_covid_received(player),
            payment_label=actual_payment_label(player),
            payment_label_with_amount=actual_payment_label_with_amount(player),
            payment_amount=payment_amount,
        )

    def error_message(player, values):
        if uses_open_descriptions(player):
            def check_open_field(first, second, total, description, label):
                if first == 'yes':
                    requires_description = True
                elif first == 'no' and second == 'decrease':
                    requires_description = False
                elif first == 'no' and second == 'same':
                    return None
                else:
                    return f"Please answer the follow-up question for {label}."

                if first == 'yes' or second == 'decrease':
                    if total is None or total <= 0:
                        return f"Please enter the amount for {label}."

                if requires_description and not (description or '').strip():
                    return f"Please answer the open-ended question for {label}."

            debt_open_error = check_open_field(
                values['debt_increase'],
                values['debt_same_or_decrease'],
                values['debt_amount'],
                values['debt_repay_description'],
                'debt repayment',
            )
            if debt_open_error:
                return debt_open_error

            spend_open_error = check_open_field(
                values['spend_increase'],
                values['spend_same_or_decrease'],
                values['spend_amount'],
                values['spending_description'],
                'spending',
            )
            if spend_open_error:
                return spend_open_error

            return None

        def check_category(first, second, total, components, label):
            if first == 'yes':
                direction = 'increase'
            elif first == 'no' and second == 'decrease':
                direction = 'decrease'
            elif first == 'no' and second == 'same':
                return None
            else:
                return f"Please answer the follow-up question for {label}."

            if total is None or total <= 0:
                return f"Please enter the amount for {label}."

            allocation_sum = sum(value or 0 for value in components)
            if abs(allocation_sum - total) > 0.01:
                return (
                    f"The amounts allocated for {label} add up to ${int(allocation_sum)}, "
                    f"but the total {direction} is ${int(total)}. Please make sure these amounts match."
                )

        debt_error = check_category(
            values['debt_increase'],
            values['debt_same_or_decrease'],
            values['debt_amount'],
            [values['debt_cc'], values['debt_long'], values['debt_short'], values['debt_bills']],
            'debt repayment',
        )
        if debt_error:
            return debt_error

        spend_error = check_category(
            values['spend_increase'],
            values['spend_same_or_decrease'],
            values['spend_amount'],
            [values['spend_everyday'], values['spend_leisure'], values['spend_services'], values['spend_durable']],
            'spending',
        )
        if spend_error:
            return spend_error

    def before_next_page(player, timeout_happened):
        if uses_open_descriptions(player):
            for field in [
                'debt_cc', 'debt_bills', 'debt_short', 'debt_long',
                'spend_everyday', 'spend_leisure', 'spend_services', 'spend_durable',
            ]:
                setattr(player, field, None)
        else:
            player.debt_repay_description = None
            player.spending_description = None

        if player.field_maybe_none('debt_increase') != 'yes' or player.field_maybe_none('debt_amount') in [None, 0]:
            player.debt_repay_description = None
        if player.field_maybe_none('spend_increase') != 'yes' or player.field_maybe_none('spend_amount') in [None, 0]:
            player.spending_description = None

        debtBaseline(player)


class TrainingRobin(Page):
    form_model = 'player'
    template_name = 'Part2/TrainingRobin.html'
    form_fields = [
        'spending_Robin',
        'save_invest_Robin',
        'debt_repay_Robin',
        'debt_new_Robin',
        'labor_Robin',
        'labor_hours_Robin',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return scenario_pronouns(player)

    @staticmethod
    def is_displayed(player: Player):
        return is_t4_training(player)

    @staticmethod
    def error_message(player, values):
        save_first_training_attempt(player, 'Robin', values)
        error = validate_training_response(
            values,
            dict(
                debt_repay_Robin=200,
                spending_Robin=500,
                debt_new_Robin=0,
                labor_Robin=0,
                labor_hours_Robin=0.0,
                save_invest_Robin=300,
            ),
            dict(
                debt_repay_Robin="Look at the first bullet: Robin repays $200 of credit card debt, so debt repayment increases by $200.",
                spending_Robin="Look at the second bullet: Robin buys a computer for $500, so spending increases by $500.",
                debt_new_Robin="Robin does not borrow or leave new bills unpaid in this example, so new debt should stay the same.",
                labor_Robin="Robin's working hours and earnings do not change in this example.",
                labor_hours_Robin="Robin's working hours do not change in this example.",
                save_invest_Robin="After $200 in debt repayment and $500 in spending, the remaining $300 is left for savings, investments, or future use.",
            )
        )
        if error:
            add_training_trial(player, 'training_trials_Robin')
            return error

    @staticmethod
    def before_next_page(player, timeout_happened):
        add_training_trial(player, 'training_trials_Robin')


class TrainingCharlie(Page):
    form_model = 'player'
    template_name = 'Part2/TrainingCharlie.html'
    form_fields = [
        'spending_Charlie',
        'save_invest_Charlie',
        'debt_repay_Charlie',
        'debt_new_Charlie',
        'labor_Charlie',
        'labor_hours_Charlie',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return scenario_pronouns(player)

    @staticmethod
    def is_displayed(player: Player):
        return is_t4_training(player)

    @staticmethod
    def error_message(player, values):
        save_first_training_attempt(player, 'Charlie', values)
        error = validate_training_response(
            values,
            dict(
                debt_repay_Charlie=600,
                spending_Charlie=200,
                debt_new_Charlie=200,
                labor_Charlie=0,
                labor_hours_Charlie=0.0,
                save_invest_Charlie=400,
            ),
            dict(
                debt_repay_Charlie="Look at the first bullet: Charlie repays $600 in credit card debt, so debt repayment increases by $600.",
                spending_Charlie="The birthday surprise counts as spending, even though Charlie pays for it with a credit card.",
                debt_new_Charlie="Because the $200 credit card charge is not repaid by the end of the month, it also counts as new debt.",
                labor_Charlie="Charlie does not change working hours or earnings in this example.",
                labor_hours_Charlie="Charlie does not change working hours in this example.",
                save_invest_Charlie="After the debt repayment, spending, and new debt are counted, the remaining $400 is left for savings, investments, or future use.",
            )
        )
        if error:
            add_training_trial(player, 'training_trials_Charlie')
            return error

    @staticmethod
    def before_next_page(player, timeout_happened):
        add_training_trial(player, 'training_trials_Charlie')


class TrainingMorgan(Page):
    form_model = 'player'
    template_name = 'Part2/TrainingMorgan.html'
    form_fields = [
        'spending_Morgan',
        'save_invest_Morgan',
        'debt_repay_Morgan',
        'debt_new_Morgan',
        'labor_Morgan',
        'labor_hours_Morgan',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return scenario_pronouns(player)

    @staticmethod
    def is_displayed(player: Player):
        return is_t4_training(player)

    @staticmethod
    def error_message(player, values):
        save_first_training_attempt(player, 'Morgan', values)
        error = validate_training_response(
            values,
            dict(
                debt_repay_Morgan=0,
                spending_Morgan=300,
                debt_new_Morgan=0,
                labor_Morgan=50,
                labor_hours_Morgan=2.0,
                save_invest_Morgan=650,
            ),
            dict(
                debt_repay_Morgan="Morgan does not repay debt in this example, so debt repayment should stay the same.",
                spending_Morgan="Look at the first bullet: Morgan buys a guitar for $300, so spending increases by $300.",
                debt_new_Morgan="Morgan does not borrow or leave new bills unpaid in this example, so new debt should stay the same.",
                labor_Morgan="Look at the second bullet: Morgan refuses a gig job that would have paid $50, so earnings decrease by $50.",
                labor_hours_Morgan="Look at the second bullet: Morgan refuses a gig job that would have taken 2 hours, so hours worked decrease by 2.",
                save_invest_Morgan="After the $300 guitar purchase and the $50 decrease in earnings, the remaining $650 is left for savings, investments, or future use.",
            )
        )
        if error:
            add_training_trial(player, 'training_trials_Morgan')
            return error

    @staticmethod
    def before_next_page(player, timeout_happened):
        add_training_trial(player, 'training_trials_Morgan')



class TrainingTransition(Page):
    form_model = 'player'
    template_name = 'Part2/TrainingTransition.html'

    @staticmethod
    def is_displayed(player: Player):
        return is_t4_training(player)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            is_t2_received=actual_stimulus_elicitation(player)
        )


class ElicitationT1(Page):
    form_model = 'player'
    form_fields = [
        # Spending
        'spend_increase', 'spend_same_or_decrease', 'spend_amount',
        'spend_everyday', 'spend_leisure', 'spend_services', 'spend_durable',

        # Debt repayment
        'debt_increase', 'debt_same_or_decrease', 'debt_amount',
        'debt_cc', 'debt_bills', 'debt_short', 'debt_long',

        # Labor
        'labor_decrease', 'labor_same_or_increase',
        'labor_hours', 'labor_income',
        'labor_gigs', 'labor_overtime', 'labor_holidays', 'labor_contract',

        # New debt
        'newdebt_increase', 'newdebt_amount','newdebt_same_or_decrease',
        'newdebt_cc', 'newdebt_bills', 'newdebt_short', 'newdebt_long',

    ]

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.subsession.Treatment == 2
            or player.subsession.Treatment == 4
            or player.subsession.Treatment == 3
            and participant_value(player, 'received_stimulus') == 2
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t4=has_training_examples(player))

    def error_message(player, values):
        def check_category(first, second, total, components, label, yes_direction='increase', no_direction='decrease'):
            if first == 'yes':
                direction = yes_direction
            elif first == 'no' and second == no_direction:
                direction = no_direction
            elif first == 'no' and second == 'same':
                return None
            else:
                return f"Please answer the follow-up question for {label}."

            if total is None or total <= 0:
                return f"Please enter the amount for {label}."

            allocation_sum = sum(value or 0 for value in components)
            if abs(allocation_sum - total) > 0.01:
                return (
                    f"The amounts allocated for {label} add up to ${int(allocation_sum)}, "
                    f"but the total {direction} is ${int(total)}. Please make sure these amounts match."
                )

        checks = [
            check_category(values['spend_increase'], values['spend_same_or_decrease'], values['spend_amount'], [
                values['spend_everyday'], values['spend_leisure'],
                values['spend_services'], values['spend_durable']
            ], 'spending'),
            check_category(values['debt_increase'], values['debt_same_or_decrease'], values['debt_amount'], [
                values['debt_cc'], values['debt_bills'],
                values['debt_short'], values['debt_long']
            ], 'debt repayment'),
            check_category(values['newdebt_increase'], values['newdebt_same_or_decrease'], values['newdebt_amount'], [
                values['newdebt_cc'], values['newdebt_bills'],
                values['newdebt_short'], values['newdebt_long']
            ], 'new debt'),
            check_category(values['labor_decrease'], values['labor_same_or_increase'], values['labor_income'], [
                values['labor_gigs'], values['labor_overtime'],
                values['labor_holidays'], values['labor_contract']
            ], 'earnings', yes_direction='decrease', no_direction='increase'),
        ]

        for error in checks:
            if error:
                return error

    def before_next_page(player, timeout_happened):
        save_elicitation_totals(player)


class ElicitationT2(Page):
    form_model = 'player'
    form_fields = [
        # Spending
        'spend_increase', 'spend_same_or_decrease', 'spend_amount',
        'spend_everyday', 'spend_leisure', 'spend_services', 'spend_durable',

        # Debt repayment
        'debt_increase', 'debt_same_or_decrease', 'debt_amount',
        'debt_cc', 'debt_bills', 'debt_short', 'debt_long',

        # Labor
        'labor_decrease', 'labor_same_or_increase',
        'labor_hours', 'labor_income',
        'labor_gigs', 'labor_overtime', 'labor_holidays', 'labor_contract',

        # New debt
        'newdebt_increase', 'newdebt_amount', 'newdebt_same_or_decrease',
        'newdebt_cc', 'newdebt_bills', 'newdebt_short', 'newdebt_long',

    ]
    @staticmethod
    def is_displayed(player: Player):
        return (
            player.subsession.Treatment == 3
            and participant_value(player, 'received_stimulus') == 1
        )

    @staticmethod
    def vars_for_template(player: Player):
        return dict(is_t4=has_training_examples(player))

    def error_message(player, values):
        def check_category(first, second, total, components, label, yes_direction='increase', no_direction='decrease'):
            if first == 'yes':
                direction = yes_direction
            elif first == 'no' and second == no_direction:
                direction = no_direction
            elif first == 'no' and second == 'same':
                return None
            else:
                return f"Please answer the follow-up question for {label}."

            if total is None or total <= 0:
                return f"Please enter the amount for {label}."

            allocation_sum = sum(value or 0 for value in components)
            if abs(allocation_sum - total) > 0.01:
                return (
                    f"The amounts allocated for {label} add up to ${int(allocation_sum)}, "
                    f"but the total {direction} is ${int(total)}. Please make sure these amounts match."
                )

        checks = [
            check_category(values['spend_increase'], values['spend_same_or_decrease'], values['spend_amount'], [
                values['spend_everyday'], values['spend_leisure'],
                values['spend_services'], values['spend_durable']
            ], 'spending'),
            check_category(values['debt_increase'], values['debt_same_or_decrease'], values['debt_amount'], [
                values['debt_cc'], values['debt_bills'],
                values['debt_short'], values['debt_long']
            ], 'debt repayment'),
            check_category(values['newdebt_increase'], values['newdebt_same_or_decrease'], values['newdebt_amount'], [
                values['newdebt_cc'], values['newdebt_bills'],
                values['newdebt_short'], values['newdebt_long']
            ], 'new debt'),
            check_category(values['labor_decrease'], values['labor_same_or_increase'], values['labor_income'], [
                values['labor_gigs'], values['labor_overtime'],
                values['labor_holidays'], values['labor_contract']
            ], 'earnings', yes_direction='decrease', no_direction='increase'),
        ]

        for error in checks:
            if error:
                return error

    def before_next_page(player, timeout_happened):
        save_elicitation_totals(player)


class SpendingPaymentMethods(Page):
    form_model = 'player'
    template_name = 'Part2/SpendingPaymentMethods.html'
    form_fields = [
        'spend_pay_credit_card',
        'spend_pay_debit_card',
        'spend_pay_cash',
        'spend_pay_bank_transfer',
        'spend_pay_bnpl',
        'spend_pay_store_financing',
        'spend_pay_bills_later',
        'spend_pay_prepaid',
        'spend_pay_other',
        'spend_cc_repaid',
        'spend_cc_fraction_paid',
        'spend_cc_remaining_timing',
        'spend_cc_timing_specify',
        'spend_other_paylater_repaid',
        'spend_other_paylater_fraction_paid',
        'spend_other_paylater_remaining_timing',
        'spend_other_paylater_timing_specify',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.field_maybe_none('spend_increase') == 'yes' and (player.field_maybe_none('spend_amount') or 0) > 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            page_title="Part 2 - Page 3/4",
            spending_amount=int(player.field_maybe_none('spend_amount') or 0),
            is_t2_received=actual_stimulus_elicitation(player),
            payment_label_with_amount=actual_payment_label_with_amount(player),
        )

    @staticmethod
    def error_message(player, values):
        spending_amount = player.field_maybe_none('spend_amount') or 0
        payment_total = sum([
            values['spend_pay_credit_card'] or 0,
            values['spend_pay_debit_card'] or 0,
            values['spend_pay_cash'] or 0,
            values['spend_pay_bank_transfer'] or 0,
            values['spend_pay_bnpl'] or 0,
            values['spend_pay_store_financing'] or 0,
            values['spend_pay_bills_later'] or 0,
            values['spend_pay_prepaid'] or 0,
            values['spend_pay_other'] or 0,
        ])
        if abs(payment_total - spending_amount) > 0.01:
            return (
                f"The amounts allocated across payment methods add up to ${int(payment_total)}, "
                f"but your spending increase is ${int(spending_amount)}. Please make sure these amounts match."
            )

        credit_card_total = values['spend_pay_credit_card'] or 0
        other_paylater_total = sum([
            values['spend_pay_bnpl'] or 0,
            values['spend_pay_store_financing'] or 0,
            values['spend_pay_bills_later'] or 0,
        ])

        def check_paylater(total, fraction_paid, remaining_timing, timing_specify, label):
            pay_verb = 'paid' if actual_stimulus_elicitation(player) else 'would pay'
            if total <= 0:
                if (
                    fraction_paid not in [None, 0]
                    or remaining_timing not in [None, '']
                    or (timing_specify or '').strip()
                ):
                    return f"Please leave the {label} follow-up fields blank unless they apply."
                return None

            if fraction_paid is None:
                return f"Please enter the share of the {label} you {pay_verb} using money from your accounts."
            if fraction_paid < 0 or fraction_paid > 100:
                return "Please enter a share between 0 and 100."
            if fraction_paid < 100:
                if not remaining_timing:
                    return "Please answer when you think you would pay the remaining amount."
                if remaining_timing == 'not_sure' and not (timing_specify or '').strip():
                    return "Please specify."

        cc_error = check_paylater(
            credit_card_total,
            values['spend_cc_fraction_paid'],
            values['spend_cc_remaining_timing'],
            values['spend_cc_timing_specify'],
            'credit card balance',
        )
        if cc_error:
            return cc_error

        other_error = check_paylater(
            other_paylater_total,
            values['spend_other_paylater_fraction_paid'],
            values['spend_other_paylater_remaining_timing'],
            values['spend_other_paylater_timing_specify'],
            'pay-later amounts',
        )
        if other_error:
            return other_error

    @staticmethod
    def before_next_page(player, timeout_happened):
        credit_card_total = player.field_maybe_none('spend_pay_credit_card') or 0
        other_paylater_total = sum([
            player.field_maybe_none('spend_pay_bnpl') or 0,
            player.field_maybe_none('spend_pay_store_financing') or 0,
            player.field_maybe_none('spend_pay_bills_later') or 0,
        ])

        def save_paylater(total, prefix):
            fraction_paid = player.field_maybe_none(f'{prefix}_fraction_paid')

            if total <= 0:
                setattr(player, f'{prefix}_repaid', None)
                setattr(player, f'{prefix}_fraction_paid', None)
                setattr(player, f'{prefix}_remaining_timing', None)
                setattr(player, f'{prefix}_timing_specify', None)
                return

            if fraction_paid is not None:
                setattr(player, f'{prefix}_repaid', total * fraction_paid / 100)
            if fraction_paid == 100:
                setattr(player, f'{prefix}_remaining_timing', None)
                setattr(player, f'{prefix}_timing_specify', None)

            if player.field_maybe_none(f'{prefix}_remaining_timing') != 'not_sure':
                setattr(player, f'{prefix}_timing_specify', None)

        save_paylater(credit_card_total, 'spend_cc')
        save_paylater(other_paylater_total, 'spend_other_paylater')


class FeedbackElicitation(Page):
    form_model = 'player'
    form_fields = [
        'categories_cover',
        'attention2',
        'categories_specify',
        'payment_intended_for',
        'payment_access',
        'payment_different_if_personal',
        'payment_different_explain',
        'final_comments',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return (
            is_baseline(player)
            or player.subsession.Treatment == 2
            or player.subsession.Treatment == 4
            or player.subsession.Treatment == 3 and participant_value(player, 'received_stimulus') == 2
            or is_t5_hypothetical(player)
        )

    @staticmethod
    def vars_for_template(player: Player):
        if uses_two_category_elicitation(player):
            categories = [
                'repaying more of your pre-existing debts',
                'spending more on goods and services',
            ]
        else:
            categories = [
                'repaying more of your pre-existing debts',
                'spending more on goods and services',
                'issuing more new debt',
                'decreasing the hours you work',
                'the amount left for savings, investments, or future use',
            ]

        return dict(
            categories=categories,
            is_t4=has_training_examples(player),
            feedback_page_title="Part 2 - Page 4/4",
        )

    def error_message(player, values):
        if values['categories_cover'] == 1 and not values['categories_specify']:
            return "Please specify which expense or use was difficult to classify."

        if values['payment_different_if_personal'] == 'Yes' and not values['payment_different_explain']:
            return "Please explain how your answers would have changed."


class FeedbackElicitationT2(Page):
    form_model = 'player'
    form_fields = [
        'categories_cover',
        'attention2',
        'categories_specify',
        'deposit_account',
        'payment_different_if_personal',
        'payment_different_explain',
        'final_comments',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return actual_stimulus_elicitation(player)

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            feedback_page_title="Part 2 - Page 4/4",
            payment_label=actual_payment_label(player),
            payment_label_with_amount=actual_payment_label_with_amount(player),
        )

    def error_message(self, values):
        if values['categories_cover'] == 1 and not values['categories_specify']:
            return "Please specify which expense or use was difficult to classify."

        dep = values.get('deposit_account')
        diff = values.get('payment_different_if_personal')
        explain = values.get('payment_different_explain')

        if dep in [2, 3, 4]:
            if diff is None:
                return 'Please answer Question 4.'

            if diff in [1, '1', 'Yes'] and not explain:
                return 'Please explain your answer to Question 4.'

class InstructionsScenarios(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return not has_training_examples(player)

    @staticmethod
    def vars_for_template(player: Player):
        if is_baseline(player):
            return dict(
                scenario_count=3,
                page_count=3,
                show_morgan_scenario=False,
            )
        return dict(
            scenario_count=3,
            page_count=3,
            show_morgan_scenario=False,
        )



class Robin(Page):
    form_model = 'player'
    form_fields = [
        'spending_Robin',
        'save_invest_Robin',
        'debt_repay_Robin',
        'debt_new_Robin',
        'labor_Robin',
        'labor_hours_Robin',
    ]


    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2

class RobinT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Robin',
        'debt_repay_Robin',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return is_baseline(player)

class Charlie(Page):
    form_model = 'player'
    form_fields = [
        'spending_Charlie',
        'save_invest_Charlie',
        'debt_repay_Charlie',
        'debt_new_Charlie',
        'labor_Charlie',
        'labor_hours_Charlie',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2

class Morgan(Page):
    form_model = 'player'
    form_fields = [
        'spending_Morgan',
        'save_invest_Morgan',
        'debt_repay_Morgan',
        'debt_new_Morgan',
        'labor_Morgan',
        'labor_hours_Morgan',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.Treatment == 2

class MorganT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Morgan',
        'debt_repay_Morgan',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return is_baseline(player)

class CharlieT0(Page):
    form_model = 'player'
    form_fields = [
        'spending_Charlie',
        'debt_repay_Charlie',
    ]

    def vars_for_template(player: Player):
        gender = player.participant.gender
        if gender == 1:
            pronoun_subject = "he"
            pronoun_object = "his"
        elif gender == 2:
            pronoun_subject = "she"
            pronoun_object = "her"
        else:
            pronoun_subject = "they"
            pronoun_object = "their"

        return dict(
            pronoun_subject=pronoun_subject,
            pronoun_object=pronoun_object,
        )

    @staticmethod
    def is_displayed(player: Player):
        return is_baseline(player)


class FeedbackScenario(Page):
    form_model = 'player'
    form_fields = [
        'categories_cover_scenario',
        'categories_specify_scenario',
        'final_comments',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        if is_baseline(player):
            return dict(
                scenario_feedback_page="Part 3 - Page 5/5",
                scenario_names="Robin, Charlie, and Morgan",
            )
        return dict(
            scenario_feedback_page="Part 3 - Page 5/5",
            scenario_names="Robin, Charlie, and Morgan",
        )


class End(Page):
    form_model = 'player'

class ProlificBack(Page):
    form_model = 'player'
    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=
            player.subsession.session.config['completionlink']
        )
#page_sequence = [InstructionsPart2,InstructionsPart2T2, instructionsT0, instructionsT1, ElicitationT1, instructionsT2, ElicitationT0,Spending,DebtRepayment, Labor,NewDebt,SavingsInvestments,  ElicitationT2, FeedbackElicitation , FeedbackElicitationT2,PaymentInterpretation,PaymentInterpretationT2, InstructionsScenarios, Robin, RobinT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]
#

page_sequence = [InstructionsPart2, InstructionsPart2T2, instructionsT0, instructionsT1, instructionsT2, ElicitationT1, ElicitationT0, ElicitationT2, SpendingPaymentMethods, FeedbackElicitation, FeedbackElicitationT2, End, ProlificBack]
#
#page_sequence = [InstructionsPart2,InstructionsPart2T2, instructionsT0, instructionsT1,  instructionsT2, ElicitationT0,ElicitationT1, ElicitationT2, FeedbackElicitation , FeedbackElicitationT2,QuestionsDebtRepay,QuestionsDebtRepayT2, QuestionsDebtNew, QuestionsDebtNewT2,PaymentInterpretation,PaymentInterpretationT2, InstructionsScenarios, Robin, RobinT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]

#page_sequence =[Robin, RobinT0, Charlie, CharlieT0, FeedbackScenario,End,ProlificBack]
