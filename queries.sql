CREATE TABLE "customer_enters" (
    "id" INTEGER,
    "count" INTEGER
);

CREATE TABLE "customer_leaves" (
    "id" INTEGER,
    "count" INTEGER
);

CREATE TABLE "customer_group_enters" (
    "id" INTEGER,
    "count" INTEGER
);

INSERT INTO "customer_enters" ("id", "count") VALUES (1, 0);
INSERT INTO "customer_leaves" ("id", "count") VALUES (1, 0);
INSERT INTO "customer_group_enters" ("id", "count") VALUES (1, 0);
