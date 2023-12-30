-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-12-2023 a las 09:27:02
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema-administrativo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infraestructura_y_equipo`
--

CREATE TABLE `infraestructura_y_equipo` (
  `id` int(11) NOT NULL,
  `jefe_departamento` varchar(255) NOT NULL,
  `jefe_area` varchar(255) NOT NULL,
  `fecha` date NOT NULL,
  `espacio_revisado` varchar(255) NOT NULL,
  `hallazgos` text NOT NULL,
  `atendido` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `infraestructura_y_equipo`
--

INSERT INTO `infraestructura_y_equipo` (`id`, `jefe_departamento`, `jefe_area`, `fecha`, `espacio_revisado`, `hallazgos`, `atendido`) VALUES
(20, 'TICS', 'Eminem', '2023-12-05', 'Patio', 'No climas', 'No'),
(22, 'B1', 'Slim Shady', '2023-12-07', 'Casa', 'Suciedad', 'No'),
(24, 'Biblioteca', 'Román', '2023-12-28', 'Biblioteca', 'Suciedad', 'No'),
(25, 'fsdfsad', 'fsadfasdvx', '2023-12-28', 'fgdfsgdsfgfd', 'gdsgsdgdfvcvb', 'No'),
(26, '', '', '2023-12-29', 'Patio', 'No climas', 'No'),
(27, '', '', '2023-12-29', 'Patio', 'No climas', 'No'),
(28, 'EDIFICIO A', 'CHAVO DEL 8', '2023-12-29', 'EDIFICIO A', 'BASURA', 'No'),
(29, 'EDIFICIO DE INGLÉS', '4', '2023-12-29', 'CASA', 'SDJKFJKSDAFHASJKFASDF', 'No'),
(30, 'dfgsdfgsdf', 'dfgdsfgcvb', '2023-12-29', 'gjhgjgfhj', 'mbnmbnkhjk', 'No'),
(31, 'Eminem', 'juasjuas', '2023-12-29', 'casa', 'yo no se', 'No'),
(32, 'sdafasdf', 'vxvcfg', '2023-12-29', 'fdsfsadf', 'pc gamer', 'No'),
(33, 'Tecnologías de la Información', 'Penjamo', '2024-02-29', 'Casa', 'Sin luz', 'No'),
(34, 'Departamento de Inglés', 'Penjamius', '2023-12-31', 'Casa', 'Casa 2', 'Sí'),
(35, 'gdgsdg', 'gsdfgsdfg', '2023-12-29', 'dsfgsdgsdfgsdgsdfgdsfg', 'gsdfgdsfgsdgsdfg', 'No'),
(36, 'kjnkjnjknk', 'knkjnjnkjnkj', '2023-12-29', 'ijopkopom', 'jnnoniooi', 'No'),
(37, 'juasjuasjuas', 'juasjuas', '2023-12-29', 'JUAS', 'NO NASODNSSAOD', 'Sí'),
(38, 'fsdfsdfsd', 'sfdsdfsadf', '2023-12-29', 'sdfsadfxcv', 'gfhdgfh', 'No'),
(39, 'fsasfsdf', '', '2023-12-29', 'cvxczvxcv', 'asfsadfsadfas', 'No'),
(40, 'fsdfsdfxvc', 'ghfhdfghdf', '2023-12-29', 'fghfdghfg', 'sadfasdfd', 'No'),
(41, 'fsdfsdfvcvx', 'fdgtrsgg', '2023-12-29', 'dgdfsgdfgdcbv', 'dfgsdfgsdfgsdfg', 'No'),
(42, 'fdgdfbvcb', 'bgnhgdhfgh', '2023-12-29', 'fdghfghfg', 'jhnmbnmb', 'No'),
(43, 'fdsfasdfasd', 'bvcbbcvbc', '2023-12-29', 'nvbncvbnvbn', 'ghjfgjguyt', 'No'),
(44, 'fdsfasdfasd', 'bvcbbcvbc', '2023-12-29', 'nvbncvbnvbn', 'ghjfgjguyt', 'No'),
(45, 'TICS', 'Eminem', '2023-12-30', 'Casa', 'No hay agua', 'Sí');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden_trabajo`
--

CREATE TABLE `orden_trabajo` (
  `NControl` varchar(255) NOT NULL,
  `TipoMantenimiento` varchar(255) NOT NULL,
  `TipoServicio` varchar(255) NOT NULL,
  `AsignadoA` varchar(255) NOT NULL,
  `Fecha` date NOT NULL,
  `TrabajoRealizado` varchar(255) NOT NULL,
  `VerificadoPor` varchar(255) NOT NULL,
  `AprobadoPor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `orden_trabajo`
--

INSERT INTO `orden_trabajo` (`NControl`, `TipoMantenimiento`, `TipoServicio`, `AsignadoA`, `Fecha`, `TrabajoRealizado`, `VerificadoPor`, `AprobadoPor`) VALUES
('18E20262', 'Externo', 'Externo', 'Bob esponja', '2023-12-29', 'Pizzaría y panadería 123', 'Mi', 'Venom'),
('xcvcxvxcv', 'dfcvbcvbcxb', 'Interno', 'xcvzxvxcvxcv', '2023-12-29', 'czxzvxvxc vvdfgdfg', 'cvbvnghjgh', 'nghngfnbvnbvc'),
('asdasdasd', 'Interno', 'fasdfasdfsadf', 'sdfasdfsvxcvxadfas', '2023-12-29', 'sfddsvgfhfgbn', 'fasdfsadfasdvzvc', 'cxvxcvfdgdsfgd'),
('18E20262', 'Externo', 'TECNOLOGIAS', 'ROBERTO', '2023-12-29', 'COMPRÓ UNA PC GAMER', 'MI', 'EMINEM'),
('FASDFAS', 'Interno', 'VDSFVDSFV', 'SADFASFAS', '2023-12-29', 'SFDASDFXCVXCVVDFG', 'SDFGSDFVC', 'XCVXCVXCV'),
('18E', 'Interno', 'GFVCBCVB', 'SFSDF', '2023-12-29', 'XVCXV FDG', 'CVBCXBVC', 'HFGHFGBV'),
('18e', 'Interno', '', '', '2023-12-29', '', '', ''),
('18E20262', 'Interno', '', '', '2023-12-29', '', '', ''),
('18E20262', 'Interno', '', '', '2023-12-29', '', '', ''),
('18E20262', 'Interno', '', '', '2023-12-29', '', '', ''),
('DFS1818S', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Externo', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', 'fsdfsdf', '', '2023-12-29', '', '', ''),
('', 'Interno', 'ñññññ', '', '2023-12-29', '', '', ''),
('', 'Interno', 'dfsdfsdf', '', '2023-12-29', '', '', ''),
('', 'Interno', 'sdfsdfcx', '', '2023-12-29', '', '', ''),
('', 'Interno', '', 'penjamo', '2023-12-29', '', '', ''),
('', 'Interno', '', 'yo', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', 'hgsadfjhsadgfshgfjshgdfgjgjdsadf', '', ''),
('', 'Interno', '', '', '2023-12-29', 'bgfbgfsbfsgbfbfsgbfsgbfsbg', '', ''),
('', 'Interno', '', '', '2023-12-29', 'gdfgdfgdfvsdfvsvdssvsfvdsvf', '', ''),
('', 'Interno', '', '', '2023-12-29', 'sfdsafsadfsfdasdfasdf', '', ''),
('', 'Interno', '', '', '2023-12-29', '', 'gdgdsgdgdfgs', ''),
('hdfgh', 'Interno', '', '', '2023-12-29', '', 'ghgdhfdghdfhdfh', ''),
('', 'Interno', '', '', '2023-12-29', '', 'hfghfdghfgh', ''),
('', 'Interno', '', '', '2023-12-29', '', 'yo', ''),
('', 'Interno', '', '', '2023-12-29', '', 'vjhkhjkhgkghjk', ''),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('', 'Interno', '', '', '2023-12-29', '', 'jkfdvhkdjfh', ''),
('', 'Interno', '', '', '2023-12-29', '', 'fasdfsdf', ''),
('', 'Interno', '', '', '2023-12-29', '', '', 'bcvbcvbcv'),
('', 'Interno', '', '', '2023-12-29', '', '', 'fgsfgd'),
('', 'Interno', '', '', '2023-12-29', '', '', ''),
('WI2345883', 'Externo', 'Completo', 'Gerencia', '2023-12-30', 'Se arreglaron los climas de mrd', 'Mi', 'Yo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `tipo`) VALUES
(1, 'Administrador'),
(2, 'Técnico'),
(3, 'Departamento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud_mantenimiento`
--

CREATE TABLE `solicitud_mantenimiento` (
  `id` int(11) NOT NULL,
  `departamentoDirigido` varchar(255) NOT NULL,
  `AreaSolicitante` varchar(255) NOT NULL,
  `NombreYFirma` varchar(255) NOT NULL,
  `Fecha` date NOT NULL,
  `DescripcionProblema` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `solicitud_mantenimiento`
--

INSERT INTO `solicitud_mantenimiento` (`id`, `departamentoDirigido`, `AreaSolicitante`, `NombreYFirma`, `Fecha`, `DescripcionProblema`) VALUES
(3, 'DGDSGSD', 'fadgadf', 'jasjoasj', '2023-12-29', 'fdbfdbsfdbsdfvdxdxdddd'),
(4, 'gdsfgsdf', 'dsgdsfgds', 'dfgsdgsdfg', '2023-12-29', 'bvnhgjghfdg'),
(5, '18100000', 'gdfgdgsdfg', 'gsdgsgdfsdfg', '2023-12-29', 'bvnvcbnvcnb'),
(6, '18100000', 'gdfgdgsdfg', 'gsdgsgdfsdfg', '2023-12-29', 'bvnvcbnvcnb'),
(7, '', '', '', '2023-12-29', ''),
(8, '', '', '', '2023-12-29', ''),
(9, '4454', 'sfdasfs', 'fsdafasdvc', '2023-12-30', 'sadfsdfcxvxcv'),
(10, 'fasdfdas', 'fsdfrhgf', 'fdsvcxvfh', '2023-12-30', 'vxckjvhjkfdsgaksldf'),
(11, 'dfasdfsadf', 'fsdfasdfasd', 'gdfbcvbcv', '2023-12-30', 'gdfgdfvcbgfhsg'),
(12, '', '', 'fsdfsafsdfsadf', '2023-12-30', ''),
(13, '', '', 'gdfgdsg', '2023-12-30', ''),
(14, '', '', 'gdfgdsgsdfg', '2023-12-30', ''),
(15, '', '', 'dfgsdfgsdbvcbcvxb', '2023-12-30', ''),
(16, '', '', 'gdgdfgdfgsdfg', '2023-12-30', ''),
(18, '', '', 'fsfsfasdf', '2023-12-30', ''),
(19, '', 'dsfgsfdgsdfg', 'gdfgdsfg', '2023-12-30', ''),
(20, '', 'fsdfsdfvxcb', '', '2023-12-30', ''),
(21, '', 'bcvbcv', '', '2023-12-30', ''),
(22, '', '', '', '2023-12-30', ''),
(23, '', '', '', '2023-12-30', ''),
(24, '', '', '', '2023-12-30', ''),
(25, '', '', '', '2023-12-30', ''),
(26, '', '', '', '2023-12-30', ''),
(27, '', '', '', '2023-12-30', ''),
(28, '', '', '', '2023-12-30', ''),
(29, '', '', '', '2023-12-30', ''),
(30, '', '', '', '2023-12-30', ''),
(31, '', '', '', '2023-12-30', ''),
(32, '', '', '', '2023-12-30', 'vbcbkcmvopbkepowrkqwe'),
(33, '', 'No c', 'Anguilloso', '2023-12-30', 'JASJSAJDJAKDJDK'),
(34, '', 'Y0', 'Penajmius', '2023-12-30', 'Ndar'),
(35, '01', 'Y0', 'Penajmius', '2023-12-30', 'Ndar'),
(37, '', 'fsfsadfsadf', 'fdsafafdadsf', '2023-12-30', 'vcxvxcvsfasdf'),
(38, '', '', '', '2023-12-30', ''),
(39, '', '', '', '2023-12-30', ''),
(40, '', 'dfgsdgsdfg', 'gdfgsdfvc', '2023-12-30', 'bcvbcvbdfsgd'),
(41, '41', 'dsfjkascndjksdc', 'fjndkjnckcd', '2023-12-30', 'SDJKWEIOJPASODISPFAO'),
(42, 'dsafpokop', 'fsdfsvcbh', 'lkjvpcoipoert', '2023-12-30', 'KASJLKSDFLKFS'),
(43, '', '', '', '2023-12-30', ''),
(44, '', '', '', '2023-12-30', ''),
(45, '', 'Recursos', '', '2023-12-30', ''),
(46, 'Penjamo', 'Recursos', '', '2023-12-30', ''),
(47, 'Penjamo', 'Recursos', 'Yo', '2023-12-30', ''),
(48, 'RH', 'Penjamo', '', '2023-12-30', ''),
(49, 'rh', '', '', '2023-12-30', ''),
(50, 'gdfgdfgvf', '', '', '2023-12-30', ''),
(51, 'hfdhfdg', '', '', '2023-12-30', ''),
(52, '', 'TICS', '', '2023-12-30', ''),
(53, '', '', 'Mi', '2023-12-30', ''),
(54, '', '', 'dfgdfsg', '2023-12-30', ''),
(55, '', '', '', '2023-12-30', 'JIJIJIJA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `user_name`, `password`, `id_rol`) VALUES
(18, 'Oscar Uriel Cruz Ruiz', '0000', 1),
(29, 'Biblioteca', 'BIBLIOTECAITSR2024', 3),
(30, 'Oscar Ruíz', '0000', 2),
(31, 'The Game', '4871', 0),
(32, 'The Game', '4871', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `infraestructura_y_equipo`
--
ALTER TABLE `infraestructura_y_equipo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `solicitud_mantenimiento`
--
ALTER TABLE `solicitud_mantenimiento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `infraestructura_y_equipo`
--
ALTER TABLE `infraestructura_y_equipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `solicitud_mantenimiento`
--
ALTER TABLE `solicitud_mantenimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
