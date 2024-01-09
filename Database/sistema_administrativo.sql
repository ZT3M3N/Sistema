-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-01-2024 a las 03:05:57
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
-- Base de datos: `sistema_administrativo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `infraestructura_y_equipo`
--

CREATE TABLE `infraestructura_y_equipo` (
  `id` int(11) NOT NULL,
  `departamento_responsable` varchar(255) NOT NULL,
  `jefe_area` varchar(255) NOT NULL,
  `jefe_departamento` varchar(255) NOT NULL,
  `fecha` date NOT NULL,
  `espacio_revisado` varchar(255) NOT NULL,
  `hallazgos` text NOT NULL,
  `atendido` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden_trabajo`
--

CREATE TABLE `orden_trabajo` (
  `id` int(11) NOT NULL,
  `NControl` varchar(255) NOT NULL,
  `TipoMantenimiento` varchar(255) NOT NULL,
  `TipoServicio` varchar(255) NOT NULL,
  `AsignadoA` varchar(255) NOT NULL,
  `Fecha` date NOT NULL,
  `TrabajoRealizado` varchar(255) NOT NULL,
  `VerificadoPor` varchar(255) NOT NULL,
  `AprobadoPor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programas_realizados`
--

CREATE TABLE `programas_realizados` (
  `id` int(11) NOT NULL,
  `Semestre` varchar(100) NOT NULL,
  `Año` int(100) NOT NULL,
  `Fecha` date NOT NULL,
  `Elaboro` varchar(255) NOT NULL,
  `Aprobo` varchar(255) NOT NULL,
  `Numero` int(255) NOT NULL,
  `Servicio` varchar(255) NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `E` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_rol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `user_name`, `password`, `id_rol`) VALUES
(31, 'Oscar Uriel Cruz Ruiz', '0000', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `infraestructura_y_equipo`
--
ALTER TABLE `infraestructura_y_equipo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `orden_trabajo`
--
ALTER TABLE `orden_trabajo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `programas_realizados`
--
ALTER TABLE `programas_realizados`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `orden_trabajo`
--
ALTER TABLE `orden_trabajo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `programas_realizados`
--
ALTER TABLE `programas_realizados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `solicitud_mantenimiento`
--
ALTER TABLE `solicitud_mantenimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
