# Patient
- first_name:       `String`
- last_name:        `String`
- date_of_birth:    `Date`
- email:            `String`
- phone:            `String`

# Appointment
- scheduled_time:   `DateTime`
- status:           `Enum`
- patient:          `FK` -> `Patient`

# Invoice
- total_amount: `Decimal`
- status:       `Enum`
- appointment:  `OneToOne` -> `Appointment`

# Notification
- message:          `Text`
- scheduled_send:   `DateTime`
- sent:             `Boolean`
- patient:          `FK` -> `Patient`
- appointment:      `FK` -> `Appointment (nullable)`