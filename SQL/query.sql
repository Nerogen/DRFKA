WITH UserLinksCount AS (
    SELECT
        user_id,
        COUNT(*) AS links_count,
        ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, registration_date ASC) AS rank
    FROM
        links_table
    GROUP BY
        user_id
)
SELECT
    users.id,
    users.email,
    users.registration_date,
    UserLinksCount.links_count
FROM
    users
JOIN
    UserLinksCount ON users.id = UserLinksCount.user_id
WHERE
    UserLinksCount.rank <= 10;
