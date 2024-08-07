use crate::nodes::*;

pub trait DynamicNode<Ix, T>: StaticNode
where
    Ix: Clone + Hash + Eq + PartialOrd,
    T: Clone,
{
    fn as_any_mute(&mut self) -> &mut dyn Any;
    fn update(&mut self, index: Ix, item: T) -> bool;
    fn empty(&self) -> bool;
    fn to_vec(&self) -> Vec<&T>;
    fn first(&self) -> Option<&T>;
    fn last(&self) -> Option<&T>;
    fn between(&self, start: Ix, end: Ix) -> Option<Vec<&T>>;
}

impl DynamicNode<Instant, f64> for Publisher {
    fn update(&mut self, index: Instant, item: f64) -> bool {
        self.sentiments.push(index, item)
    }

    fn empty(&self) -> bool {
        self.sentiments.empty()
    }

    fn to_vec(&self) -> Vec<&f64> {
        self.sentiments.to_vec()
    }

    fn first(&self) -> Option<&f64> {
        self.sentiments.first()
    }

    fn last(&self) -> Option<&f64> {
        self.sentiments.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&f64>> {
        self.sentiments.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, PriceAggregate> for Currency {
    fn update(&mut self, index: Instant, item: PriceAggregate) -> bool {
        self.history.push(index, item)
    }

    fn empty(&self) -> bool {
        self.history.empty()
    }

    fn to_vec(&self) -> Vec<&PriceAggregate> {
        self.history.to_vec()
    }

    fn first(&self) -> Option<&PriceAggregate> {
        self.history.first()
    }

    fn last(&self) -> Option<&PriceAggregate> {
        self.history.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&PriceAggregate>> {
        self.history.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, PriceAggregate> for Equity {
    fn update(&mut self, index: Instant, item: PriceAggregate) -> bool {
        self.history.push(index, item)
    }

    fn empty(&self) -> bool {
        self.history.empty()
    }

    fn to_vec(&self) -> Vec<&PriceAggregate> {
        self.history.to_vec()
    }

    fn first(&self) -> Option<&PriceAggregate> {
        self.history.first()
    }

    fn last(&self) -> Option<&PriceAggregate> {
        self.history.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&PriceAggregate>> {
        self.history.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, PriceAggregate> for Bonds {
    fn update(&mut self, index: Instant, item: PriceAggregate) -> bool {
        self.history.push(index, item)
    }

    fn empty(&self) -> bool {
        self.history.empty()
    }

    fn to_vec(&self) -> Vec<&PriceAggregate> {
        self.history.to_vec()
    }

    fn first(&self) -> Option<&PriceAggregate> {
        self.history.first()
    }

    fn last(&self) -> Option<&PriceAggregate> {
        self.history.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&PriceAggregate>> {
        self.history.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, OptionsAggregate> for Options {
    fn update(&mut self, index: Instant, item: OptionsAggregate) -> bool {
        self.history.push(index, item)
    }

    fn empty(&self) -> bool {
        self.history.empty()
    }

    fn to_vec(&self) -> Vec<&OptionsAggregate> {
        self.history.to_vec()
    }

    fn first(&self) -> Option<&OptionsAggregate> {
        self.history.first()
    }

    fn last(&self) -> Option<&OptionsAggregate> {
        self.history.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&OptionsAggregate>> {
        self.history.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, FinancialStatement> for Company
{
    fn update(&mut self, index: Instant, item: FinancialStatement) -> bool {
        match item {
            FinancialStatement::IncomeStatement(item) => self.income_statement.push(index, item),
            FinancialStatement::BalanceSheet(item) => self.balance_sheet.push(index, item),
            FinancialStatement::CashFlow(item) => self.cash_flow.push(index, item),
            FinancialStatement::Earnings(item) => self.earnings.push(index, item),
        }
    }

    fn empty(&self) -> bool {
        false
    }

    fn to_vec(&self) -> Vec<&FinancialStatement> {
        Vec::new()
    }

    fn first(&self) -> Option<&FinancialStatement> {
        None
    }

    fn last(&self) -> Option<&FinancialStatement> {
        None
    }

    fn between(&self, _: Instant, _: Instant) -> Option<Vec<&FinancialStatement>> {
        None
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, IncomeStatement> for Company {
    fn update(&mut self, index: Instant, item: IncomeStatement) -> bool {
        self.income_statement.push(index, item)
    }

    fn empty(&self) -> bool {
        self.income_statement.empty()
    }

    fn to_vec(&self) -> Vec<&IncomeStatement> {
        self.income_statement.to_vec()
    }

    fn first(&self) -> Option<&IncomeStatement> {
        self.income_statement.first()
    }

    fn last(&self) -> Option<&IncomeStatement> {
        self.income_statement.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&IncomeStatement>> {
        self.income_statement.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, BalanceSheet> for Company {
    fn update(&mut self, index: Instant, item: BalanceSheet) -> bool {
        self.balance_sheet.push(index, item)
    }

    fn empty(&self) -> bool {
        self.balance_sheet.empty()
    }

    fn to_vec(&self) -> Vec<&BalanceSheet> {
        self.balance_sheet.to_vec()
    }

    fn first(&self) -> Option<&BalanceSheet> {
        self.balance_sheet.first()
    }

    fn last(&self) -> Option<&BalanceSheet> {
        self.balance_sheet.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&BalanceSheet>> {
        self.balance_sheet.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, CashFlow> for Company {
    fn update(&mut self, index: Instant, item: CashFlow) -> bool {
        self.cash_flow.push(index, item)
    }

    fn empty(&self) -> bool {
        self.cash_flow.empty()
    }

    fn to_vec(&self) -> Vec<&CashFlow> {
        self.cash_flow.to_vec()
    }

    fn first(&self) -> Option<&CashFlow> {
        self.cash_flow.first()
    }

    fn last(&self) -> Option<&CashFlow> {
        self.cash_flow.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&CashFlow>> {
        self.cash_flow.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}

impl DynamicNode<Instant, Earnings> for Company {
    fn update(&mut self, index: Instant, item: Earnings) -> bool {
        self.earnings.push(index, item)
    }

    fn empty(&self) -> bool {
        self.earnings.empty()
    }

    fn to_vec(&self) -> Vec<&Earnings> {
        self.earnings.to_vec()
    }

    fn first(&self) -> Option<&Earnings> {
        self.earnings.first()
    }

    fn last(&self) -> Option<&Earnings> {
        self.earnings.last()
    }

    fn between(&self, start: Instant, end: Instant) -> Option<Vec<&Earnings>> {
        self.earnings.between(&start, &end)
    }

    fn as_any_mute(&mut self) -> &mut dyn Any {
        self
    }
}
