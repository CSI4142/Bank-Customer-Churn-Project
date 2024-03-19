-- SQL scripts related to banking profile dimension

-- SQL command to set primary key constraint on banking profile dimension
ALTER TABLE `csi4142.churn_dataset.Banking Profile`
ADD PRIMARY KEY (Bank_Profile_Key) NOT ENFORCED;