-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jun 03, 2022 at 03:55 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_class`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `bio` longtext NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `firstname`, `lastname`, `phone`, `profile_pic`, `address`, `bio`, `username`, `email`, `user_id`) VALUES
(1, '', '', '', 'static/default_user.png', '', '', 'newuser', 'newuser@gmail.com', 6),
(2, 'Pradip', 'Kandel', '9843624525', 'static/uploads/download_DrcTMqB.jpg', 'Gulmi', 'Offcanvas is a sidebar component that can be toggled via JavaScript to appear from the left, right, or bottom edge of the viewport. Buttons or anchors are used as triggers that are attached to specific elements you toggle, and data attributes are used to invoke our JavaScript.', 'rajesh', 'rajesh@gmail.com', 7),
(3, '', '', '', 'static/default_user.png', '', '', 'pradip123', 'pradeepkandel008@gmail.com', 8);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add product', 7, 'add_product'),
(26, 'Can change product', 7, 'change_product'),
(27, 'Can delete product', 7, 'delete_product'),
(28, 'Can view product', 7, 'view_product'),
(29, 'Can add student', 8, 'add_student'),
(30, 'Can change student', 8, 'change_student'),
(31, 'Can delete student', 8, 'delete_student'),
(32, 'Can view student', 8, 'view_student'),
(33, 'Can add file upload', 9, 'add_fileupload'),
(34, 'Can change file upload', 9, 'change_fileupload'),
(35, 'Can delete file upload', 9, 'delete_fileupload'),
(36, 'Can view file upload', 9, 'view_fileupload'),
(37, 'Can add profile', 10, 'add_profile'),
(38, 'Can change profile', 10, 'change_profile'),
(39, 'Can delete profile', 10, 'delete_profile'),
(40, 'Can view profile', 10, 'view_profile'),
(41, 'Can add cart', 11, 'add_cart'),
(42, 'Can change cart', 11, 'change_cart'),
(43, 'Can delete cart', 11, 'delete_cart'),
(44, 'Can view cart', 11, 'view_cart'),
(45, 'Can add order', 12, 'add_order'),
(46, 'Can change order', 12, 'change_order'),
(47, 'Can delete order', 12, 'delete_order'),
(48, 'Can view order', 12, 'view_order');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(6, 'pbkdf2_sha256$260000$ED0BzuefK4yKFy8Ls0rlpF$0KQJ6e/8Y9CdUXi4FiH19lXEIglU4rWKECg4hdXJZYs=', '2022-05-26 01:25:07.383645', 1, 'newuser', '', '', 'newuser@gmail.com', 1, 1, '2022-05-26 01:12:26.186586'),
(7, 'pbkdf2_sha256$260000$TpTqRzh8BOhoL7dW6gLU9j$6KOrDvFPv8FjGi6TQLxQJcJ7Wo6QL6OsiBl7v5AqHjM=', '2022-06-01 01:00:43.620733', 0, 'rajesh', '', '', 'rajesh@gmail.com', 0, 1, '2022-05-26 01:43:52.432194'),
(8, 'pbkdf2_sha256$260000$0rlEHILFdPXMMUzDht5T2R$T7QdrRBjCmlc7JwcSSJuNzyb8k2BHAPLdaQGbfAk0KI=', '2022-06-01 01:19:43.692792', 0, 'pradip123', '', '', 'pradeepkandel008@gmail.com', 0, 1, '2022-06-01 01:14:41.383941');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'accounts', 'profile'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'products', 'cart'),
(9, 'products', 'fileupload'),
(12, 'products', 'order'),
(7, 'products', 'product'),
(8, 'products', 'student'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-05 01:05:18.038233'),
(2, 'auth', '0001_initial', '2022-05-05 01:05:19.289230'),
(3, 'admin', '0001_initial', '2022-05-05 01:05:19.523229'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-05 01:05:19.537230'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-05 01:05:19.568230'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-05 01:05:19.721231'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-05 01:05:19.818228'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-05 01:05:19.862236'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-05 01:05:19.877229'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-05 01:05:19.933227'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-05 01:05:19.937226'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-05 01:05:19.959248'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-05 01:05:19.985231'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-05 01:05:20.009242'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-05 01:05:20.036230'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-05 01:05:20.052229'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-05 01:05:20.088231'),
(18, 'products', '0001_initial', '2022-05-05 01:05:20.214229'),
(19, 'products', '0002_product_category', '2022-05-05 01:05:20.230230'),
(20, 'sessions', '0001_initial', '2022-05-05 01:05:20.432228'),
(21, 'products', '0003_student', '2022-05-05 01:14:05.067040'),
(22, 'products', '0004_fileupload', '2022-05-08 01:28:19.772111'),
(23, 'products', '0005_student_email', '2022-05-18 00:57:08.522318'),
(24, 'accounts', '0001_initial', '2022-05-26 01:06:45.427357'),
(25, 'products', '0006_auto_20220526_0651', '2022-05-26 01:06:45.442356'),
(26, 'products', '0007_cart_order', '2022-06-01 01:33:49.046353');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ufvk4c718bl0p9o9rz6918ds7p1tnodn', '.eJxVjMEOwiAQBf-FsyGUwgIevfcbCLCLVA0kpT0Z_9026UGvb2bem_mwrcVvnRY_I7syyy6_WwzpSfUA-Aj13nhqdV3myA-Fn7TzqSG9bqf7d1BCL3utpB0UODCIQucYs9aCHICRQjsVdIrSKjQD7RyIIANamYwacYwyoGGfL83jN7k:1nwD1T:H5Xat13t30W3xSTMGzDsHhtwtsjcZOxY8jRu-9JvfC4', '2022-06-15 01:19:43.695775');

-- --------------------------------------------------------

--
-- Table structure for table `products_cart`
--

CREATE TABLE `products_cart` (
  `id` bigint(20) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_cart`
--

INSERT INTO `products_cart` (`id`, `created_date`, `product_id`, `user_id`) VALUES
(9, '2022-06-03 01:45:07.840032', 1, 8),
(10, '2022-06-03 01:45:12.869506', 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `products_fileupload`
--

CREATE TABLE `products_fileupload` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_fileupload`
--

INSERT INTO `products_fileupload` (`id`, `title`, `description`, `image`) VALUES
(11, 'May15', 'Lorem', 'static/uploads/iamge2_IdS6zBL.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `products_order`
--

CREATE TABLE `products_order` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `status` varchar(200) NOT NULL,
  `payment_method` varchar(200) NOT NULL,
  `payment_status` tinyint(1) NOT NULL,
  `contact_no` varchar(10) NOT NULL,
  `contact_address` varchar(200) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `product_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_order`
--

INSERT INTO `products_order` (`id`, `quantity`, `total_price`, `status`, `payment_method`, `payment_status`, `contact_no`, `contact_address`, `created_date`, `product_id`, `user_id`) VALUES
(2, 1, 6000, 'Pending', 'Esewa', 1, '9843624525', 'Sankhamul', '2022-06-03 01:35:51.062911', 3, 8),
(3, 5, 5995, 'Pending', 'Esewa', 1, '9843624525', 'Sankhamul', '2022-06-03 01:37:57.106491', 1, 8),
(4, 10, 15990, 'Pending', 'Esewa', 1, '9843624522', 'Baneshwor', '2022-06-03 01:43:56.266992', 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `products_product`
--

CREATE TABLE `products_product` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `stock` int(11) NOT NULL,
  `image_url` varchar(2000) NOT NULL,
  `category` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_product`
--

INSERT INTO `products_product` (`id`, `name`, `price`, `stock`, `image_url`, `category`) VALUES
(1, 'Football', 1199, 5, 'https://www.planetware.com/wpimages/2019/12/nepal-in-pictures-beautiful-places-to-photograph-annapurna-range.jpg', 'Sports'),
(2, 'Data Science', 1599, 9, 'https://previews.123rf.com/images/metelsky/metelsky1904/metelsky190400020/121859822-male-avatar-icon-or-portrait-handsome-young-man-face-businessman-in-suit-and-necktie-vector-illustra.jpg', 'Books'),
(3, 'Mobile', 6000, 7, 'http://cdn.mos.cms.futurecdn.net/6t8Zh249QiFmVnkQdCCtHK.jpg', 'Electronics');

-- --------------------------------------------------------

--
-- Table structure for table `products_student`
--

CREATE TABLE `products_student` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(200) NOT NULL,
  `lastname` varchar(200) NOT NULL,
  `batch` int(11) NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `email` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_student`
--

INSERT INTO `products_student` (`id`, `firstname`, `lastname`, `batch`, `image_url`, `created_date`, `email`) VALUES
(6, 'Saphal123', 'Shrestha123', 29, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-10 01:23:29.472149', NULL),
(8, 'p', 'p', 1000000, 'dasffsagd', '2022-05-18 00:59:50.572120', 'pradeepkandel008@gmail.com'),
(9, 'pr', 'pr', 100, 'https://previews.123rf.com/images/metelsky/metelsky1904/metelsky190400020/121859822-male-avatar-icon-or-portrait-handsome-young-man-face-businessman-in-suit-and-necktie-vector-illustra.jpg', '2022-05-18 01:11:39.934910', 'pradeepkandel008@gmail.com'),
(10, 'P', 'p', 105, 'https://images-na.ssl-images-amazon.com/images/I/51if47n2aPL._AC_SL1000_.jpg', '2022-05-18 01:15:03.785782', NULL),
(11, 'Pradip', 'Kandel', 27, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-18 01:18:46.628945', 'pradeepkandel008@gmail.com'),
(12, 'Pradip', 'Kandel', 27, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-18 01:33:49.248353', 'pradeepkandel008@gmail.com'),
(13, 'Pradip', 'Kandel', 27, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-18 01:38:01.718390', 'pradeepkandel008@gmail.com'),
(14, 'Pradip', 'Kandel', 99, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-18 01:40:13.683158', 'pradeepkandel008@gmail.com'),
(15, 'Pradip', 'Kandel', 27, 'https://st2.depositphotos.com/3557671/11164/v/950/depositphotos_111644880-stock-illustration-man-avatar-icon-of-vector.jpg', '2022-05-29 01:12:14.995119', 'pradeepkandel008@gmail.com'),
(16, 'Rajendra', 'Kandel', 34, 'https://images-na.ssl-images-amazon.com/images/I/51if47n2aPL._AC_SL1000_.jpg', '2022-05-29 01:12:24.283484', 'rajurajkandel@gmail.com'),
(17, 'Pradip', 'Kandel', 23, 'https://images-na.ssl-images-amazon.com/images/I/51if47n2aPL._AC_SL1000_.jpg', '2022-05-29 01:12:33.069329', 'pradeepkandel008@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `products_cart`
--
ALTER TABLE `products_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `products_cart_product_id_52080291_fk_products_product_id` (`product_id`),
  ADD KEY `products_cart_user_id_d53bf7cf_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `products_fileupload`
--
ALTER TABLE `products_fileupload`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products_order`
--
ALTER TABLE `products_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `products_order_product_id_a3214026_fk_products_product_id` (`product_id`),
  ADD KEY `products_order_user_id_dfb540d8_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `products_product`
--
ALTER TABLE `products_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products_student`
--
ALTER TABLE `products_student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `products_cart`
--
ALTER TABLE `products_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `products_fileupload`
--
ALTER TABLE `products_fileupload`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `products_order`
--
ALTER TABLE `products_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `products_product`
--
ALTER TABLE `products_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `products_student`
--
ALTER TABLE `products_student`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `products_cart`
--
ALTER TABLE `products_cart`
  ADD CONSTRAINT `products_cart_product_id_52080291_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  ADD CONSTRAINT `products_cart_user_id_d53bf7cf_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `products_order`
--
ALTER TABLE `products_order`
  ADD CONSTRAINT `products_order_product_id_a3214026_fk_products_product_id` FOREIGN KEY (`product_id`) REFERENCES `products_product` (`id`),
  ADD CONSTRAINT `products_order_user_id_dfb540d8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
