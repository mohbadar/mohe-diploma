CREATE TABLE `appointments` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `center_id` int NOT NULL,
  `queue_no` int DEFAULT '0',
  `appointment_date` date NOT NULL,
  `start_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `end_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `family_form_reference_no` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `appointments_appointment_date_index` (`appointment_date`),
  KEY `appointments_family_form_reference_no_index` (`family_form_reference_no`),
  KEY `appointments_center_id_index` (`center_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17544 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci