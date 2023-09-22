CREATE TABLE Company (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE FinancialData (
    data_id INT SERIAL PRIMARY KEY,
    company_id INT SERIAL,
    fiscalDateEnding DATE NOT NULL,
    reportedCurrency VARCHAR(5) NOT NULL,
    totalAssets BIGINT,
    cashAndShortTermInvestments BIGINT,
    inventory BIGINT,
    currentNetReceivables BIGINT,
    totalNonCurrentAssets BIGINT,
    propertyPlantEquipment BIGINT,
    accumulatedDepreciationAmortizationPPE BIGINT,
    intangibleAssets BIGINT,
    goodwill BIGINT,
    FOREIGN KEY company_id
);

