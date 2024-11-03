-- Tabela Paciente
CREATE TABLE IF NOT EXISTS medsched_db.Paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_nascimento DATE,
    endereco VARCHAR(150),
    telefone VARCHAR(15)
);

-- Tabela Médico
CREATE TABLE IF NOT EXISTS medsched_db.Medico (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    especialidade VARCHAR(50),
    telefone VARCHAR(15)
);

-- Tabela Consulta
CREATE TABLE IF NOT EXISTS medsched_db.Consulta (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    data_consulta DATETIME,
    motivo VARCHAR(200),
    FOREIGN KEY (id_paciente) REFERENCES medsched_db.Paciente(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES medsched_db.Medico(id_medico)
);

-- Inserção de Dados na Tabela Paciente
INSERT INTO medsched_db.Paciente (nome, cpf, data_nascimento, endereco, telefone)
VALUES 
('Ana Silva', '12345678901', '1990-01-15', 'Rua A, 123', '11987654321'),
('Carlos Pereira', '23456789012', '1985-03-22', 'Av. B, 456', '11987654322'),
('Mariana Souza', '34567890123', '1992-07-30', 'Rua C, 789', '11987654323'),
('Pedro Santos', '45678901234', '1980-05-10', 'Av. D, 101', '11987654324'),
('Beatriz Lima', '56789012345', '1995-11-25', 'Rua E, 102', '11987654325'),
('Lucas Fernandes', '67890123456', '1987-08-12', 'Av. F, 103', '11987654326');

-- Inserção de Dados na Tabela Médico
INSERT INTO medsched_db.Medico (nome, cpf, especialidade, telefone)
VALUES 
('Dr. João Costa', '78901234567', 'Cardiologia', '11987654327'),
('Dra. Carla Ribeiro', '89012345678', 'Dermatologia', '11987654328'),
('Dr. Paulo Souza', '90123456789', 'Ortopedia', '11987654329'),
('Dra. Renata Lima', '01234567890', 'Pediatria', '11987654330'),
('Dr. Ricardo Alves', '12345678902', 'Neurologia', '11987654331'),
('Dra. Fernanda Oliveira', '23456789013', 'Oftalmologia', '11987654332');

-- Inserção de Dados na Tabela Consulta
INSERT INTO medsched_db.Consulta (id_paciente, id_medico, data_consulta, motivo)
VALUES 
(1, 1, '2024-11-15 09:00:00', 'Consulta de rotina'),
(2, 2, '2024-11-16 10:30:00', 'Exame dermatológico'),
(3, 3, '2024-11-17 08:00:00', 'Consulta pós-operatória'),
(4, 4, '2024-11-18 11:00:00', 'Consulta pediátrica'),
(5, 5, '2024-11-19 14:30:00', 'Avaliação neurológica'),
(6, 6, '2024-11-20 16:00:00', 'Exame de vista');
